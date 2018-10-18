from django.views.generic import ListView, DetailView

from . import models
# from .models import *


class ShowProduct(ListView):
    template_name = 'product.html'
    queryset = models.products.objects.all()


class ProductDetail(DetailView):
    model = models.products
    template_name = 'detail.html'


