# Generated by Django 2.0rc1 on 2017-12-30 14:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0004_item_variation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='variation',
        ),
    ]
