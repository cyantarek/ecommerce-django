# Generated by Django 2.0rc1 on 2017-12-27 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_auto_20171227_1823'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='sale_price',
            field=models.DecimalField(blank=True, decimal_places=2, default=29.99, max_digits=100, null=True),
        ),
    ]