from django.contrib.auth import forms as auth_forms, get_user_model, login
from django.contrib.auth import views as auth_views
from django.contrib.auth import mixins as auth_mixins
from django.urls import reverse_lazy
from django.views import generic as views

from CarsAPI.authentication.forms import UserRegistrationForm

UserModel = get_user_model()


class UserRegistrationView(views.CreateView):
    form_class = UserRegistrationForm
    template_name = 'user_register.html'
    success_url = reverse_lazy('list create user car')

    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, self.object)
        return result


class UserLoginView(auth_views.LoginView):
    template_name = 'user_login.html'

    def get_success_url(self):
        next = self.request.GET.get('next', None)
        if next:
            return next
        return reverse_lazy('list create user car')


class UserLogoutView(auth_views.LogoutView):
    pass
