from django.db import models

# Create your models here.
from django.db import models
#from django.contrib.auth.models import AbstractUser
#from django.contrib.auth.models import Group
#from utils.main import disable_for_loaddata
from django.db.models.signals import post_save


class Managers(models.Model):
    manager_name = models.CharField(max_length=20, blank=True, null=True, default=None, verbose_name="имя менеджера")
    manager_phone = models.CharField(max_length=11, blank=True, null=True, default=None, verbose_name="телефон менеджера")

    def __str__(self):
        return "%s" % self.manager_name

    class Meta:
        verbose_name = 'менеджер'
        verbose_name_plural = 'менеджеры'


class Shops(models.Model):
    adress = models.CharField(max_length=50, blank=True, null=True, default=None, verbose_name="адрес")
    manager_name = models.ForeignKey(Managers, blank=True, null=True, default=None, on_delete=models.CASCADE, verbose_name="менеджер")
    shop_phone = models.CharField(max_length=11, blank=True, null=True, default=None,verbose_name="телефон магазина")
    active = models.BooleanField(default=True)

    def __str__(self):
        return "%s" % self.adress

    class Meta:
        verbose_name = 'Магазин'
        verbose_name_plural = 'Магазины'


class Sellers(models.Model):
    seller_name = models.CharField(max_length=20, blank=True, null=True, default=None, verbose_name="имя продавца")
    adress = models.ForeignKey(Shops, blank=True, null=True, default=None, on_delete=models.CASCADE, verbose_name="адрес магазина")
    seller_phone = models.CharField(max_length=11, blank=True, null=True, default=None, verbose_name="телефон продавца")
    active = models.BooleanField(default=True)

    def __str__(self):
        return "%s" % self.seller_name

    class Meta:
        verbose_name = 'Продавец'
        verbose_name_plural = 'Продавцы'


class Suppliers(models.Model):
    supplier_inn = models.CharField(max_length=10, blank=True, null=True, default=None, verbose_name="ИНН поставщика")
    supplier_name = models.CharField(max_length=20, blank=True, null=True, default=None, verbose_name="Название поставщика")
    supplier_adress = models.CharField(max_length=20, blank=True, null=True, default=None, verbose_name="адрес поставщика")
    supplier_phone = models.CharField(max_length=20, blank=True, null=True, default=None, verbose_name="телефон поставщика")
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="добавлен")

    def __str__(self):
        return " %s" % self.supplier_name

    class Meta:
        verbose_name = 'поставщик'
        verbose_name_plural = 'Поставщики'


class Products(models.Model):
    name = models.CharField(max_length=20, blank=True, null=True, default=None, verbose_name="наименование")
    price_opt = models.DecimalField(max_digits=10, decimal_places=0, default=0, verbose_name="оптовая цена")
    price = models.DecimalField(max_digits=10, decimal_places=0, default=0, verbose_name="розничная цена")
    left = models.DecimalField(max_digits=10, decimal_places=0, default=0, verbose_name="остаток в наличии")
    supplier = models.ForeignKey(Suppliers, blank=True, null=True, default=None, on_delete=models.CASCADE, verbose_name="поставщик")
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="добавлен")
    updated = models.DateTimeField(auto_now_add=False, auto_now=True, verbose_name="изменен")

    def __str__(self):
        return "%s, %s" % (self.id, self.name)

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'Товары'

    def save(self, *args, **kwargs):
        self.price = 2 * self.price_opt

        super(Products, self).save(*args, **kwargs)


class Accounts(models.Model):
    data_account = models.DateTimeField(blank=True, null=True, default=None, verbose_name="дата записи")
    seller_name = models.ForeignKey(Sellers, max_length=20, blank=True, null=True, default=None, on_delete=models.CASCADE, verbose_name="имя продавца")
    total_count = models.DecimalField(max_digits=10, decimal_places=0, default=0, verbose_name="единиц товара продано")
    total_price = models.DecimalField(max_digits=10, decimal_places=0, default=0, verbose_name="сумма продажи")
 #   total_price_opt = models.DecimalField(max_digits=10, decimal_places=0, default=0, verbose_name="суммарная оптовая стоимость")
    revenue = models.DecimalField(max_digits=10, decimal_places=0, default=0, verbose_name="выручка")
    updated = models.DateTimeField(auto_now_add=False, auto_now=True, verbose_name="изменен")

    def __str__(self):
        return "%s" % self.id

    class Meta:
        verbose_name = 'продажи'
        verbose_name_plural = 'Журнал счетов'


class ProductInAccount(models.Model):
    account = models.ForeignKey(Accounts, blank=True, null=True, default=True, on_delete=models.CASCADE, verbose_name="номер записи")
    product = models.ForeignKey(Products, blank=True, null=True, default=True, on_delete=models.CASCADE, verbose_name="наименование")
    nmb = models.IntegerField(default=1, verbose_name="количество")
    price_per_item = models.DecimalField(max_digits=10, decimal_places=0, default=0, verbose_name="стоимость")
    price_per_item_opt = models.DecimalField(max_digits=10, decimal_places=0, default=0, verbose_name="оптовая стоимость")
    total_price = models.DecimalField(max_digits=10, decimal_places=0, default=0, verbose_name="суммарная стоимость")  # price*nmb
    total_price_opt = models.DecimalField(max_digits=10, decimal_places=0, default=0, verbose_name="суммарная оптовая стоимость")
    total_count = models.DecimalField(max_digits=10, decimal_places=0, default=0, verbose_name="суммарное количество")

    def __str__(self):
        return self.product.name


    class Meta:
        verbose_name = "Товар в счете"
        verbose_name_plural = "Товары в счете"

    def save(self, *args, **kwargs):
        self.price_per_item = self.product.price
        self.price_per_item_opt = self.product.price_opt
        self.total_price = self.nmb * self.price_per_item
        self.total_price_opt = self.nmb * self.price_per_item_opt
        self.total_count += self.nmb

        super(ProductInAccount, self).save(*args, **kwargs)


def product_in_account_post_save(sender, instance, created, **kwargs):
    account = instance.account
    account_total_price = 0
    account_total_price_opt = 0
    account_total_count = 0
    account_revenue = 0
    all_products_in_account = ProductInAccount.objects.filter(account=account)

    for item in all_products_in_account:
        item.product.left = int(item.product.left) - int(item.nmb)
        item.product.save()
        account_total_price += item.total_price
        account_total_price_opt += item.total_price_opt
        account_total_count += item.total_count
        account_revenue = account_total_price - account_total_price_opt

    instance.account.total_count = account_total_count
    instance.account.total_price = account_total_price
    instance.account.total_price_opt = account_total_price_opt
    instance.account.revenue = account_revenue
    instance.account.save(force_update=True)


post_save.connect(product_in_account_post_save, sender=ProductInAccount)


class Request(models.Model):
    TYPE_CHOICES = (('processed', 'обработана'), ('not processed', 'не обработана'))
    date = models.DateTimeField(verbose_name='Дата')
    status = models.CharField(max_length=20, blank=True, verbose_name="статус", choices=TYPE_CHOICES)
    products = models.TextField(blank=True, verbose_name="Товары для отгрузки")
    manager_name = models.ForeignKey(Managers, on_delete=models.CASCADE, blank=True, null=True, verbose_name="Имя менеджера")

    class Meta:
        verbose_name = "заявка на поступление товаров"
        verbose_name_plural = "заявки на поступление товаров"

    def __str__(self):
        return "заявка %s" % (self.id)