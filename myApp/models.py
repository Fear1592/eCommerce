from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название категории')
    icon = models.ImageField(upload_to='category/', verbose_name='Изображение категории')

    class Meta:
        ordering = ['id']
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class ChoiceCategory(models.Model):
    name = models.CharField(max_length=150, verbose_name='Категория разновидности товара')

    class Meta:
        ordering = ['id']
        verbose_name = "Подкатегория"
        verbose_name_plural = "Подкатегории"

    def __str__(self):
        return self.name


class Choices(models.Model):
    choices_name = models.ForeignKey(ChoiceCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=150, verbose_name='Имя типа товара цвет/вкус')
    icon = models.ImageField(upload_to='choices/', verbose_name='Главное изображение разновидности товара')
    in_stock = models.BooleanField(default=True, verbose_name='В наличии')
    count = models.PositiveIntegerField(default=0, verbose_name='Колличество товара')

    class Meta:
        ordering = ['id']
        verbose_name = "Разновидность товара"
        verbose_name_plural = "Разновидности товаров"

    def __str__(self):
        return self.name


class Order(models.Model):
    STATUS_LIST = [
        ('N', 'New'),
        ('W', 'Waiting'),
        ('C', 'Cancel'),
        ('R', 'Ready pay'),
        ('D', 'On delivery'),
        ('Dd', 'Delivered'),
    ]
    status = models.CharField(max_length=50, choices=STATUS_LIST, verbose_name='Статус заказа')

    class Meta:
        ordering = ['id']
        verbose_name = "Статус заказа"
        verbose_name_plural = "Статусы заказов"

    def __str__(self):
        return self.status


class ItemInfo(models.Model):
    specifications = models.TextField(max_length=555, verbose_name='Характеристики')
    equipment = models.TextField(max_length=555, verbose_name='Комплектация')

    class Meta:
        ordering = ['id']
        verbose_name = "Описание товара"
        verbose_name_plural = "Описания товаров"

    def __str__(self):
        return str(self.specifications)


class Icon(models.Model):
    name = models.CharField(max_length=155, verbose_name='Название общих изображений товаров')
    all_icon = models.ImageField(upload_to='all_icon/', verbose_name='Общие изображения товаров')

    class Meta:
        ordering = ['id']
        verbose_name = "Изображения товара"
        verbose_name_plural = "Изображения товаров"

    def __str__(self):
        return str(self.name)


class Item(models.Model):
    name = models.CharField(max_length=155, verbose_name='Название товара')
    choice = models.ForeignKey(Choices, blank=True, null=True,
                               verbose_name='Название подкатегории',
                               on_delete=models.CASCADE)
    all_icon = models.ForeignKey(Icon, blank=True, null=True,
                                 verbose_name='Все изображения товара',
                                 on_delete=models.CASCADE)
    info_item = models.ForeignKey(ItemInfo,
                                  verbose_name='Основная информация о товаре',
                                  on_delete=models.CASCADE)
    price = models.PositiveIntegerField(verbose_name='Цена товара')
    hot = models.BooleanField(default=False, verbose_name='Популярное')
    discount = models.BooleanField(default=False, verbose_name='Наличие скидки')
    category = models.ForeignKey(Category,
                                 verbose_name='Категория товара',
                                 on_delete=models.CASCADE)
    is_published = models.BooleanField(default=False, verbose_name='Опбуликовано')
    date = models.DateTimeField(auto_now=True, verbose_name='Дата публикации')

    class Meta:
        ordering = ['-date']
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    def __str__(self):
        return str(self.name)


class Profile(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=155, null=True, blank=True, verbose_name='Имя пользователя')
    bio = models.TextField(max_length=1000, null=True, blank=True, verbose_name='Описание')
    profile_pic = models.ImageField(null=True, blank=True,
                                    upload_to="images/profile/",
                                    verbose_name='Фото профиля')
    vk = models.CharField(max_length=50, null=True, blank=True,
                          verbose_name='Профиль вконтакте')
    inst = models.CharField(max_length=50, null=True, blank=True,
                            verbose_name='Профиль в инсте')
    telegram = models.CharField(max_length=50, null=True, blank=True,
                                verbose_name='Ссылка телеграм')
    favourites = models.ForeignKey(Item, verbose_name='Избранное',
                                   on_delete=models.CASCADE,
                                   blank=True,
                                   null=True)
    order = models.ForeignKey(Order, verbose_name='Заказ',
                              on_delete=models.CASCADE,
                              blank=True,
                              null=True, )

    class Meta:
        ordering = ['id']
        verbose_name = "Профиль юзера"
        verbose_name_plural = "Профили юзеров"

    def __str__(self):
        return str(self.user)
