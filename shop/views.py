from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from .models import Category, Product, Order, OrderStatus


def categories_view(request):
    return render(request, 'shop/index.html', {
        'categories': Category.objects.all(),
    })


def category_detail(request, category_id: int):
    return render(request, 'shop/category_detail.html', {
        'category': get_object_or_404(Category, id=category_id),
    })


def products_view(request):
    return render(request, 'shop/products.html', {
        'products': Product.objects.all(),
    })


def product_detail(request, product_id: int):
    return render(request, 'shop/product_detail.html', {
        'product': get_object_or_404(Product, id=product_id),
    })


def add_to_cart(request):
    assert request.method == 'POST'
    product_id = request.POST['product_id']
    if not request.user.is_authenticated:
        product_url = reverse('shop:product_detail', args=[product_id])
        redirect_url = reverse('login') + '?next=' + product_url
        return HttpResponseRedirect(redirect_url)
    product = get_object_or_404(Product, id=product_id)
    request.user.profile.ensure_shopping_cart().add_product(product)
    return redirect('shop:product_detail', product_id)


@login_required
def shopping_cart(request):
    request.user.profile.ensure_shopping_cart()
    return render(request, 'shop/shopping_cart.html')


@login_required
def submit_order(request):
    profile = request.user.profile
    order = profile.shopping_cart
    order.status = OrderStatus.COMPLETED
    order.save()
    profile.shopping_cart = Order.objects.create(profile=profile)
    profile.save()
    return render(request, 'shop/order_successfully_submitted.html', {'order': order})

