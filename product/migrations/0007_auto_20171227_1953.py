# Generated by Django 2.0rc1 on 2017-12-27 13:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_auto_20171227_1947'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='products/images/')),
                ('featured', models.BooleanField(default=False)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('thumbnail', models.BooleanField(default=False)),
            ],
        ),
        migrations.RemoveField(
            model_name='product',
            name='image',
        ),
        migrations.AddField(
            model_name='productimage',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.Product'),
        ),
    ]
