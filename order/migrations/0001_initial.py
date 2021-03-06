# Generated by Django 2.0rc1 on 2017-12-30 18:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cart', '0005_remove_item_variation'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.CharField(default='ABCD', max_length=120, unique=True)),
                ('status', models.CharField(choices=[('Started', 'Started'), ('Abandoned', 'Abandoned'), ('Finished', 'Finished')], default='started', max_length=120)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cart.Cart')),
            ],
        ),
    ]
