from django.contrib import admin
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from django.urls import path

app_name = 'portfolio'

urlpatterns = [
    path('', views.home, name='home'),
    url(r'^home/$', views.home, name='home'),
    path('customer_list', views.customer_list, name='customer_list'),
    path('customer/create', views.customer_new, name='customer_new'),
    path('customer/<int:pk>/edit/', views.customer_edit, name='customer_edit'),
    path('customer/<int:pk>/portfolio/', views.customer_portfolio, name='customer_portfolio'),
    path('customer/<int:pk>/delete/', views.customer_delete, name='customer_delete'),

    path('stock_list', views.stock_list, name='stock_list'),
    path('stock/create', views.stock_new, name='stock_new'),
    path('stock/<int:pk>/edit/', views.stock_edit, name='stock_edit'),
    path('stock/<int:pk>/delete/', views.stock_delete, name='stock_delete'),

    path('investment_list', views.investment_list, name='investment_list'),
    path('investment/create', views.investment_new, name='investment_new'),
    path('investment/<int:pk>/edit/', views.investment_edit, name='investment_edit'),
    path('investment/<int:pk>/delete/', views.investment_delete, name='investment_delete'), 

    url(r'^customers_json/', views.CustomerList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)