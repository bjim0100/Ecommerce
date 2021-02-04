from rest_framework import serializers

from Products.models import ProductModel, AddtoCartModel


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductModel
        fields = [
            'id',
            'title',
            'price',
            'description',
            'image1',
            'image2',
            'image3',
            'category',
            'date',

        ]


class AddtoCartSerializer(serializers.ModelSerializer):
    product_name = serializers.StringRelatedField(source='product')

    class Meta:
        model = AddtoCartModel
        fields = [
            'product_name',
            'quantity'
        ]


class AddtoCartView(serializers.ModelSerializer):
    product_name = serializers.StringRelatedField(source='product')

    class Meta:
        model = AddtoCartModel
        fields = [
            'product_name',
            'quantity'
        ]
