from django.urls import path
from CarsAPI.api import views

urlpatterns = (
    path('car-brands/', views.CarBrandListCreateView.as_view(), name='list create car brand '),
    path('car-brands/<int:pk>/', views.CarBrandEditDeleteView.as_view(), name='edit delete car brand'),
    path('car-models/', views.CarModelListCreateView.as_view(), name='list create car model'),
    path('car-models/<int:pk>/', views.CarModelDeleteEditView.as_view(), name='edit delete car model'),
    path('user-cars/', views.UserCarCreateListView.as_view(), name='list create user car'),
    path('user-cars/<int:pk>/', views.UserCarDeleteEditView.as_view(), name='edit delete user car'),

)
