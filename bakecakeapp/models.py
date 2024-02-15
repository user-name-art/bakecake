from django.db import models


class User(models.Model):  # todo replace with custom user
    name = models.CharField('Имя', max_length=50)

    def __str__(self):
        return self.name


class Order(models.Model):
    user = models.ForeignKey(
        'User',
        on_delete=models.CASCADE,
        related_name='orders',
        null=True
    )
    cost = models.DecimalField('Стоимость', max_digits=7, decimal_places=2)
    text = models.CharField('Надпись', max_length=60, blank=True)
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
        return self.user.name


class Cake(models.Model):
    title = models.CharField('Наименование', max_length=50)
    cost = models.DecimalField('Стоимость', max_digits=7, decimal_places=2)

    text = models.CharField('Надпись', max_length=60, blank=True)
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
