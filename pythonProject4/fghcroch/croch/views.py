from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.shortcuts import *
from django.urls import reverse_lazy
from django.views.generic import *
from .forms import *
from .models import *


class CrochHome(ListView):
    model = Products
    context_object_name = 'products'
    template_name = 'croch/index.html'
    extra_context = {'title': 'Главная страница'}


def about(request):
    context = {'title': 'Контакты'}
    return render(request, 'croch/contacts.html', context=context)


class ContactFormView(FormView):
    form_class = ContactForm
    template_name = 'croch/support.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        print(form.cleaned_data)
        return redirect('home')


class ShowProducts(DetailView):
    model = Products
    template_name = 'croch/product.html'
    slug_url_kwarg = 'product_slug'
    context_object_name = 'product'


class ProdCategory(ListView):
    model = Products
    template_name = 'croch/index.html'
    context_object_name = 'products'
    extra_context = {'title': 'Товары'}

    def get_queryset(self):
        return Products.objects.filter(cat__slug=self.kwargs['cat_slug']).select_related('cat')

class AddProd(CreateView):
    form_class = AddProdForm
    template_name = 'croch/add_prod.html'


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'croch/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'croch/login.html'


def logout_user(request):
    logout(request)
    return redirect('login')

