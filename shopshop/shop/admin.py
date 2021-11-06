from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django import forms
from .models import *
from django.contrib.admin import SimpleListFilter
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from shop.models import *
from django.contrib.admin import AdminSite


class ProductsAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = [field.name for field in Products._meta.fields]

    class Meta:
        model = Products


admin.site.register(Products, ProductsAdmin)


class SellersAdmin(admin.ModelAdmin):
    search_fields = ['seller_name']
    list_display = [field.name for field in Sellers._meta.fields]

    class Meta:
        model = Sellers


admin.site.register(Sellers, SellersAdmin)


class ManagersAdmin(admin.ModelAdmin):
    search_fields = ['manager_name']
    list_display = [field.name for field in Managers._meta.fields]

    class Meta:
        model = Managers


admin.site.register(Managers, ManagersAdmin)

class ShopsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Shops._meta.fields]

    class Meta:
        model = Shops


admin.site.register(Shops, ShopsAdmin)


class SuppliersAdmin(admin.ModelAdmin):
    search_fields = ['supplier_name']
    list_display = [field.name for field in Suppliers._meta.fields]

    class Meta:
        model = Suppliers


admin.site.register(Suppliers, SuppliersAdmin)


class ProductInAccountInline(admin.TabularInline):
    model = ProductInAccount
    extra = 0


class AccountsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Accounts._meta.fields]
    inlines = [ProductInAccountInline]

    class Meta:
        model = Accounts

admin.site.register(Accounts, AccountsAdmin)


class ProductInAccountAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ProductInAccount._meta.fields]

    class Meta:
        model = ProductInAccount


admin.site.register(ProductInAccount, ProductInAccountAdmin)


class RequestAdmin(admin.ModelAdmin):
    list_filter=['status']
    list_display = [field.name for field in Request._meta.fields]

    class Meta:
        model = Request


admin.site.register(Request, RequestAdmin)


