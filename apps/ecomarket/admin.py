from django.contrib import admin

from .models import Category, Product, Cart, CartItem

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    fields = ("image", "name")


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    fields = ("image", "name", "price", "description", "category")


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    fields = ("product",)


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    fields = ("product", "quantity")

