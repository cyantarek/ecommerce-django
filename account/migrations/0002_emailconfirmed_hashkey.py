# Generated by Django 2.0rc1 on 2018-01-05 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='emailconfirmed',
            name='hashkey',
            field=models.CharField(default='123456789', max_length=120),
        ),
    ]
