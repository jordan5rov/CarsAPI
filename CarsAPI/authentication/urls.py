from django.urls import path
from CarsAPI.authentication import views

urlpatterns = (
    path('register/', views.UserRegistrationView.as_view(), name='register user'),
    path('login/', views.UserLoginView.as_view(), name='login user'),
    path('logout/', views.UserLogoutView.as_view(), name='logout user'),
)
