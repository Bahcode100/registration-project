from django.urls import path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('customers', views.CustomerViewSet)

urlpatterns = [
    path('', views.index, name='home'),
    path('customer/', views.customer, name='customer'),
    path('customer/update/<int:pk>/', views.update, name='update'),
    path('customer/delete/<int:pk>/', views.delete, name='delete'),
    path('customer/detail/<int:pk>/', views.customer_detail, name='detail')
] + router.urls
