# Generated by Django 2.1.5 on 2019-08-06 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20190806_0922'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='conversion_rate',
            field=models.IntegerField(default=0),
        ),
    ]
