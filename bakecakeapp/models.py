from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from phonenumber_field.modelfields import PhoneNumberField
from .managers import CustomUserManager


class Level(models.Model):
    cake_level = models.IntegerField(verbose_name='Количество уровней')
    price = models.DecimalField('Стоимость', max_digits=7, decimal_places=2)

    def __str__(self):
        return f'{self.cake_level}'


class Shape(models.Model):
    shape_name = models.CharField(max_length=30, verbose_name='Форма')
    price = models.DecimalField('Стоимость', max_digits=7, decimal_places=2)

    def __str__(self):
        return self.shape_name


class Topping(models.Model):
    topping_name = models.CharField(max_length=30, verbose_name='Топпинг')
    price = models.DecimalField('Стоимость', max_digits=7, decimal_places=2)

    def __str__(self):
        return self.topping_name


class Berry(models.Model):
    berry_name = models.CharField(max_length=30, verbose_name='Ягоды')
    price = models.DecimalField('Стоимость', max_digits=7, decimal_places=2)

    def __str__(self):
        return self.berry_name


class Decor(models.Model):
    decor_name = models.CharField(max_length=30, verbose_name='Декор')
    price = models.DecimalField('Стоимость', max_digits=7, decimal_places=2)

    def __str__(self):
        return self.decor_name


class CustomCake(models.Model):
    level_count = models.ForeignKey(
        Level,
        verbose_name='Количество уровней',
        related_name='levels',
        on_delete=models.CASCADE
    )
    shape = models.ForeignKey(
        Shape,
        verbose_name='Форма',
        related_name='shapes',
        on_delete=models.CASCADE
    )
    topping = models.ForeignKey(
        Topping,
        verbose_name='Топпинг',
        related_name='toppings',
        on_delete=models.CASCADE
    )
    berry = models.ForeignKey(
        Berry,
        verbose_name='Ягоды',
        related_name='berries',
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    decor = models.ForeignKey(
        Decor,
        verbose_name='Декор',
        related_name='decors',
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    text = models.CharField(
        max_length=200,
        verbose_name='Надпись на торте',
        blank=True,
        null=True
    )

    def __str__(self):
        return f'Cake level {self.level_count}, shape {self.shape}'


class CustomUser(AbstractBaseUser, PermissionsMixin):
    name = models.CharField('Имя клиента', max_length=50, null=True, blank=True)
    phone_number = PhoneNumberField('номер телефона', unique=True)
    email = models.EmailField('электронная почта', unique=True, null=True, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return str(self.phone_number)


class Order(models.Model):
    STATUS = (
        ('a', 'Принят'),
        ('p', 'Готовится'),
        ('d', 'Доставляется'),
        ('c', 'Выполнен'),
    )

    user = models.ForeignKey(
        'CustomUser',
        on_delete=models.CASCADE,
        related_name='orders',
        null=True
    )
    cost = models.DecimalField('Стоимость', max_digits=7, decimal_places=2)
    comment = models.TextField('Комментарий', blank=True)
    custom_cake = models.ForeignKey(
        'CustomCake',
        on_delete=models.CASCADE,
        related_name='order',
        null=True)

    cakes = models.ManyToManyField(
        'Cake',
        verbose_name='Торты',
        related_name='orders',
        blank=True,
    )
    address = models.CharField(
        max_length=200,
        verbose_name='адрес доставки',
        default='самовывоз'
    )
    created_date = models.DateTimeField('Дата создания', auto_now_add=True)
    delivery_date = models.DateTimeField('Дата доставки', null=True, blank=True)
    status = models.CharField(
        max_length=20,
        verbose_name='Статус заказа',
        choices=STATUS,
        default='a'
    )

    def __str__(self):
        return f'{self.id}, {self.created_date}, {self.user.phone_number}'


class Cake(models.Model):
    title = models.CharField('Наименование', max_length=50)
    cost = models.DecimalField('Стоимость', max_digits=7, decimal_places=2)
    image = models.ImageField('Изображение', blank=True)
    description = models.TextField('Описание', blank=True)

    def __str__(self):
        return self.title
