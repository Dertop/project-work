from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.shortcuts import get_object_or_404

from api.models import Category, Furniture
from api.serializers import UserSerializer, CategorySerializer, FurnitureSerializer, OrderSerializer
from rest_framework.pagination import LimitOffsetPagination


class CategoryListView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CategorySerializer
    permission_classes = (AllowAny,)
    lookup_url_kwarg = 'id'

    def get_queryset(self):
        id = self.kwargs['id']
        return Category.objects.filter(id=id)


class CategoryFurnitureList(generics.ListAPIView):
    serializer_class = FurnitureSerializer

    def get_queryset(self):
        category_id = self.kwargs.get('id')
        return Furniture.objects.filter(category_id=category_id)


class FurnitureListView(generics.ListCreateAPIView):
    serializer_class = FurnitureSerializer
    permission_classes = (AllowAny,)
    queryset = Furniture.objects.all()


class FurnitureDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Furniture.objects.all()
    serializer_class = FurnitureSerializer
    lookup_field = 'id'

    def get_queryset(self):
        id = self.kwargs['id']
        return Furniture.objects.filter(id=id)
