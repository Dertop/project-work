from django.shortcuts import render
from django.http.response import JsonResponse
from models import User, Category, Furniture, Order
from django.views.decorators.csrf import csrf_exempt
from .serializers import UserSerializer, CategorySerializer, FurnitureSerializer, OrderSerializer
from rest_framework import generics
import json


class CategoryListView(generics.ListCreateAPIView):
    # permission_classes = [IsAuthenticated]
    queryset = Category.objects.all()
    serializer_class = CategorySerialaizer


class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = [IsAuthenticated]
    queryset = Category.objects.all()
    serializer_class = CourseSerializer


class ModuleListView(generics.ListCreateAPIView):
    # permission_classes = [IsAuthenticated]
    serializer_class = ModuleSerializer

    def get_queryset(self):
        course_id = self.kwargs.get('pk')
        print("get", self.kwargs)
        return Module.objects.filter(course_id=course_id)

    def perform_create(self, serializer):
        course_id = self.kwargs.get('pk')
        serializer.save(course_id=course_id)


class ModuleDetailView(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = [IsAuthenticated]
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer
    lookup_url_kwarg = 'module_id'


class CoursePricingListView(generics.ListCreateAPIView):
    # permission_classes = [IsAuthenticated]
    serializer_class = CoursePricingSerializer

    def get_queryset(self):
        course_id = self.kwargs['pk']
        return CoursePricing.objects.filter(course_id=course_id)

    def perform_create(self, serializer):
        course_id = self.kwargs.get('pk')
        serializer.save(course_id=course_id)


class PricingDetailView(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = [IsAuthenticated]
    queryset = CoursePricing.objects.all()
    serializer_class = CoursePricingSerializer
    lookup_url_kwarg = 'pricing_id'


class RegisterView(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        refresh = RefreshToken.for_user(user)

        return Response({
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        })

