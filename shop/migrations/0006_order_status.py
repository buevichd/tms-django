# Generated by Django 4.1.7 on 2023-05-16 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_product_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(default='INITIAL', max_length=20),
        ),
    ]