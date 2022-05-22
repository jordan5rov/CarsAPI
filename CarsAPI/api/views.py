from django.contrib.auth import get_user_model
from rest_framework import generics as api_views

from CarsAPI.api.models import CarBrand, CarModel, UserCar
from CarsAPI.api.serializers import FullCarBrandSerializer, FullCarModelSerializer, CreateUpdateCarModelSerializer, \
    FullUserCarSerializer, CreateUpdateUserCarSerializer

UserModel = get_user_model()


class CarBrandListCreateView(api_views.ListCreateAPIView):
    serializer_class = FullCarBrandSerializer
    permission_classes = ()

    def get_queryset(self):
        query = self.request.query_params.get('brand', None)
        if not query:
            return CarBrand.objects.all()
        return CarBrand.objects.filter(name=query)


class CarBrandEditDeleteView(api_views.RetrieveUpdateDestroyAPIView):
    queryset = CarBrand.objects.all()
    serializer_class = FullCarBrandSerializer
    permission_classes = ()


class CarModelListCreateView(api_views.ListCreateAPIView):
    serializer_class = FullCarModelSerializer
    permission_classes = ()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CreateUpdateCarModelSerializer
        return FullCarModelSerializer

    def get_queryset(self):
        brand_query = self.request.query_params.get('brand', None)
        model_query = self.request.query_params.get('model', None)
        if not brand_query and not model_query:
            return CarModel.objects.all()
        if brand_query:
            brand = CarBrand.objects.get(name=brand_query)
            return CarModel.objects.filter(car_brand=brand.pk)
        return CarModel.objects.filter(name=model_query)


class CarModelDeleteEditView(api_views.RetrieveUpdateDestroyAPIView):
    queryset = CarModel.objects.all()
    serializer_class = FullCarBrandSerializer
    permission_classes = ()

    def get_serializer_class(self):
        if self.request.method == 'PUT':
            return CreateUpdateCarModelSerializer
        return FullCarModelSerializer


class UserCarCreateListView(api_views.ListCreateAPIView):
    serializer_class = FullUserCarSerializer
    permission_classes = ()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CreateUpdateUserCarSerializer
        return FullUserCarSerializer

    def get_queryset(self):
        brand_query = self.request.query_params.get('brand', None)
        model_query = self.request.query_params.get('model', None)
        user_query = self.request.query_params.get('user_id', None)
        if not brand_query and not model_query and not user_query:
            return UserCar.objects.all()
        if brand_query:
            brand = CarBrand.objects.get(name=brand_query)
            return UserCar.objects.filter(car_brand=brand.pk)
        if model_query:
            model = CarModel.objects.get(name=model_query)
            return UserCar.objects.filter(car_model=model.pk)
        user = UserModel.objects.get(pk=user_query)
        return UserCar.objects.filter(user=user.pk)


class UserCarDeleteEditView(api_views.RetrieveUpdateDestroyAPIView):
    queryset = UserCar.objects.all()
    serializer_class = FullUserCarSerializer

    def get_serializer_class(self):
        if self.request.method == 'PUT':
            return CreateUpdateUserCarSerializer
        return FullUserCarSerializer
