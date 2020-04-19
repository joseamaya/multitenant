from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet

from store.models import Category, Product
from store.serializers import CategorySerializer, ProductSerializer


class CategoryViewSet(ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class ProductsViewSet(ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()