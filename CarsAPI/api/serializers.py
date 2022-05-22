from django.contrib.auth import get_user_model
from rest_framework import serializers

from CarsAPI.api.models import CarBrand, CarModel, UserCar

UserModel = get_user_model()


class FullCarBrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarBrand
        fields = (
            'id',
            'name',
            'created_at'
        )


class IdAndNameCarBrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarBrand
        fields = (
            'id',
            'name'
        )


class CreateUpdateCarModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = (
            'id',
            'name',
            'car_brand',
        )


class FullCarModelSerializer(serializers.ModelSerializer):
    car_brand = IdAndNameCarBrandSerializer(many=False)

    class Meta:
        model = CarModel
        fields = (
            'id',
            'name',
            'created_at',
            'updated_at',
            'car_brand'
        )


class IdAndEmailUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = (
            'id',
            'email',
        )


class IdAndNameCarModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = (
            'id',
            'name',
        )


class FullUserCarSerializer(serializers.ModelSerializer):
    user = IdAndEmailUserSerializer(many=False)
    car_brand = IdAndNameCarBrandSerializer(many=False)
    car_model = IdAndNameCarModelSerializer(many=False)

    class Meta:
        model = UserCar
        fields = (
            'id',
            'first_reg',
            'odometer',
            'user',
            'car_brand',
            'car_model',
        )


class CreateUpdateUserCarSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCar
        fields = (
            'id',
            'first_reg',
            'odometer',
            'user',
            'car_brand',
            'car_model',
        )

