from rest_framework import serializers

from store.models import Category, Product


class CategorySerializer(serializers.ModelSerializer):
    pass

    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    pass

    class Meta:
        model = Product
        fields = '__all__'