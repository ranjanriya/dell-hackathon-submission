# Generated by Django 2.1.5 on 2019-08-07 15:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_auto_20190807_1530'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='product',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to='shop.Product'),
        ),
    ]
