# Generated by Django 4.1.7 on 2023-03-31 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0005_alter_item_choice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='all_icon',
            field=models.ManyToManyField(blank=True, null=True, related_name='item_as_all_icon', to='myApp.icon', verbose_name='Все изображения товара'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='favourites',
            field=models.ManyToManyField(blank=True, null=True, related_name='profile_as_favourites', to='myApp.item', verbose_name='Избранное'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='order',
            field=models.ManyToManyField(blank=True, null=True, related_name='profile_as_order', to='myApp.order', verbose_name='Заказ'),
        ),
    ]