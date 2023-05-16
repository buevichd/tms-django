from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField(default=0.0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                 related_name='products')

    def __str__(self):
        return self.name


class OrderEntry(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='+')
    count = models.IntegerField(default=0)
    order = models.ForeignKey('Order', on_delete=models.CASCADE, related_name='order_entries')

    def __str__(self):
        return f'{self.product} - {self.count}'

    @property
    def price(self):
        return self.product.price * self.count


class OrderStatus(models.TextChoices):
    INITIAL = "IN", _("Initial")
    COMPLETED = "CO", _("Completed")
    DELIVERED = "DE", _("Delivered")


class Order(models.Model):
    profile = models.ForeignKey('Profile', on_delete=models.CASCADE, related_name='orders')
    status = models.CharField(max_length=2, choices=OrderStatus.choices,
                              default=OrderStatus.INITIAL)

    def __str__(self):
        return f'id:{self.id} - {self.profile} - {self.status}'

    def add_product(self, product: Product):
        order_entry = self.order_entries.filter(product=product).first()
        if not order_entry:
            order_entry = OrderEntry(product=product, count=0, order=self)
        order_entry.count += 1
        order_entry.save()

    @property
    def price(self):
        return sum(order_entry.price for order_entry in self.order_entries.all())

    @property
    def product_count(self):
        return sum(order_entry.count for order_entry in self.order_entries.all())

    def is_empty(self):
        return not self.order_entries.exists()


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    shopping_cart = models.OneToOneField(Order, on_delete=models.SET_NULL,
                                         null=True, blank=True, related_name='+')

    def __str__(self):
        return str(self.user)

    def ensure_shopping_cart(self):
        if not self.shopping_cart:
            self.shopping_cart = Order.objects.create(profile=self)
            self.save()
        return self.shopping_cart
