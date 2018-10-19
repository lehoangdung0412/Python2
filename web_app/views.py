from django.views.generic import ListView, DetailView,CreateView
from django.urls import reverse_lazy
from . import models


class ShowProduct(ListView):
    template_name = 'web_app/product.html'
    queryset = models.products.objects.all()


class ProductDetail(DetailView):
    model = models.products
    template_name = 'web_app/detail.html'


class OrdersCreate(CreateView):
    model = models.orders
    fields = ['status', 'total']
    success_url = reverse_lazy('web_app:product')


class ShowCategory(ListView):
    template_name = 'web_app/category.html'
    queryset = models.categories.objects.all()


class DetailCategory(DetailView):
    template_name = 'web_app/detailCat.html'
    model = models.categories
