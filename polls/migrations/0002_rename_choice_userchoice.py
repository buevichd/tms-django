# Generated by Django 4.1.7 on 2023-04-03 18:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Choice',
            new_name='UserChoice',
        ),
    ]
