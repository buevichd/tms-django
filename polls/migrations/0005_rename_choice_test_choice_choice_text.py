# Generated by Django 4.1.7 on 2023-04-03 18:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_alter_choice_question'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choice',
            old_name='choice_test',
            new_name='choice_text',
        ),
    ]
