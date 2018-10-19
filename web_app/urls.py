from django.urls import path

from . import views

app_name = 'web_app'

urlpatterns = [
    path('', views.ShowCategory.as_view(), name='category'),
    # path('product/', views.ShowProduct.as_view(), name='product'),
    path('<int:pk>/', views.DetailCategory.as_view(), name='detailCat'),
    path('detail/<int:pk>/', views.ProductDetail.as_view(), name='detail'),
    path('orders/create/', views.OrdersCreate.as_view(), name='create_order'),
    path('orders/update/<int:pk>/', views.OrdersCreate.as_view(), name='create_order'),


]