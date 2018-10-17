from django.views.generic import ListView

from . import models


class ShowProduct(ListView):
    template_name = 'product.html'
    queryset = models.products.objects.all()
