from rest_framework import serializers

from .models import Category, Product, Cart, CartItem


class CategorySerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=30)

    class Meta:
        model = Category
        fields = ("image", "name")


class ProductSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=30)

    class Meta:
        model = Product
        fields = ("image", "name", "price", "description", "category")


class CartSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = Cart
        fields = ("product",)


class CartItemSerializer(serializers.ModelSerializer):
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = CartItem
        fields = ('product', 'quantity', 'total_price')

    def get_total_price(self, obj):
        total_price = 0

        if obj.product:
            total_price += obj.product.price * obj.quantity
        return total_price

