# Generated by Django 4.1.7 on 2023-05-16 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_orderentry_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('IN', 'Initial'), ('CO', 'Completed'), ('DE', 'Delivered')], default='IN', max_length=2),
        ),
    ]