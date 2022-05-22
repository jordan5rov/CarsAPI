from django.urls import path
from CarsAPI.web import views

urlpatterns = (
    path('', views.HomeView.as_view(), name='home page'),
)