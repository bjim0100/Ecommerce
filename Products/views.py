import django_filters
from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend, OrderingFilter
from rest_framework import generics, mixins, filters
from rest_framework.filters import SearchFilter

from Products.models import ProductModel, AddtoCartModel
from Products.serializers import ProductSerializer, AddtoCartSerializer, AddtoCartView


class AllProduct(generics.GenericAPIView, mixins.CreateModelMixin, mixins.ListModelMixin):
    serializer_class = ProductSerializer
    queryset = ProductModel.objects.all()

    search_fields = ['title', 'price', 'category']
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title', 'price', 'category']


    def get(self, request):
        return self.list(request)


class AddProduct(generics.GenericAPIView, mixins.CreateModelMixin, mixins.ListModelMixin):
    serializer_class = ProductSerializer
    queryset = ProductModel.objects.all()

    def post(self, request):
        return self.create(request)


class ProductDetails(generics.GenericAPIView, mixins.UpdateModelMixin, mixins.RetrieveModelMixin,
                     mixins.DestroyModelMixin):
    serializer_class = ProductSerializer
    queryset = ProductModel.objects.all()

    def put(self, request, pk):
        return self.update(request, pk)

    def get(self, request, pk):
        return self.retrieve(request, pk)

    def delete(self, request, pk):
        return self.destroy(request, pk)


class AddtoCart(generics.GenericAPIView, mixins.CreateModelMixin, mixins.ListModelMixin):
    serializer_class = AddtoCartSerializer
    queryset = AddtoCartModel.objects.all()

    def post(self, request):
        return self.create(request)


class AddtoCartView(generics.ListAPIView):
    serializer_class = AddtoCartView
    queryset = AddtoCartModel.objects.all()

    filter_backends = [filters.SearchFilter]
    search_fields = ['product__title']

    # def get(self, request):
    #     return self.list(request)

