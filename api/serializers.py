# -*- coding: utf-8 -*-

from rest_framework import serializers
from .models import Customer, CustomerFavoriteProduct


class CustomerSerializer(serializers.ModelSerializer):

    class Meta:

        model = Customer
        fields = '__all__'


class CustomerFavoriteProductSerializer(serializers.ModelSerializer):

    class Meta:

        model = CustomerFavoriteProduct
        fields = '__all__'
        extra_kwargs = {
            'customer': {
                'write_only': True
            }
        }

class CustomerFavoriteProductDetailSerializer(serializers.ModelSerializer):

    class Meta:

        model = CustomerFavoriteProduct
        fields = [
            'id',
            'product_id',
            'product_title',
            'product_price',
            'product_image',
            'review_score',
            'created_at',
            'updated_at'
        ]
        extra_kwargs = {
            'id': {
                'read_only': True
            },
            'created_at': {
                'read_only': True
            },
            'updated_at': {
                'read_only': True
            },
            'review_score': {
                'required': False
            }
        }
