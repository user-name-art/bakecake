from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from phonenumber_field.modelfields import PhoneNumberField
from .managers import CustomUserManager


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
    user = models.ForeignKey(
        'CustomUser',
        on_delete=models.CASCADE,
        related_name='orders',
        null=True
    )
    cost = models.DecimalField('Стоимость', max_digits=7, decimal_places=2)
    comment = models.TextField('Комментарий', blank=True)

    cakes = models.ManyToManyField(
        'Cake',
        verbose_name='Торты',
        related_name='orders',
        blank=True,
    )

    compositions = models.ManyToManyField(
        'Composition',
        verbose_name='Композиции',
        related_name='orders',
        blank=True,
    )

    created_date = models.DateTimeField('Дата создания', auto_now_add=True)
    delivery_date = models.DateTimeField('Дата доставки')
    status = models.BooleanField('Статус заказа', default=True)

    def __str__(self):
        return str(self.user.phone_number)

class Cake(models.Model):
    title = models.CharField('Наименование', max_length=50)
    cost = models.DecimalField('Стоимость', max_digits=7, decimal_places=2)
    image = models.ImageField('Изображение', blank=True)
    description = models.TextField('Описание', blank=True)

    def __str__(self):
        return self.title


class Composition(models.Model):
    title = models.CharField('Наименование', max_length=50)
    cost = models.DecimalField('Стоимость', max_digits=7, decimal_places=2)

    category = models.ForeignKey(
        'CompositionType',
        on_delete=models.CASCADE,
        related_name='compositions'
    )

    def __str__(self):
        return self.title


class CompositionType(models.Model):
    title = models.CharField('Наименование', max_length=50)

    def __str__(self):
        return self.title
