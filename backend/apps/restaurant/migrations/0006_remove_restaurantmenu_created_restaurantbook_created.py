# Generated by Django 4.1.3 on 2022-12-13 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0005_restaurantmenu_created'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restaurantmenu',
            name='created',
        ),
        migrations.AddField(
            model_name='restaurantbook',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
