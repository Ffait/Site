from django.urls import path, re_path

from .views import *
from croch import views

urlpatterns = [
    path('', CrochHome.as_view(), name='home'),
    path('product/<slug:product_slug>/', ShowProducts.as_view(), name='product'),
    path('category/<slug:cat_slug>/', ProdCategory.as_view(), name='category'),
    path('contacts', about, name="contacts"),
    path('add_prod', AddProd.as_view(), name='add_product'),
    path('login/', LoginUser.as_view(), name="login"),
    path('register/', RegisterUser.as_view(), name="register"),
    path('logout/', logout_user, name="logout"),
    path('support', ContactFormView.as_view(), name="support")
]