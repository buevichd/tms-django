# Generated by Django 4.1.7 on 2023-05-14 16:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_alter_profile_shopping_cart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='shopping_cart',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='shop.order'),
        ),
    ]
