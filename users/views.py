from users.models import Users
from django.urls import reverse_lazy
from django.views.generic import CreateView

from users.forms import UserRegisterForm


class UserCreateView(CreateView):
    model = Users
    form_class = UserRegisterForm
    success_url = reverse_lazy('users:login')
    template_name = 'users/user_form.html'

    def form_valid(self, form):
        user = form.save()
        user.is_active = False






from django.shortcuts import render

# Create your views here.
