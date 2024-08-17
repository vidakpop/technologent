from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('product/<int:pk>',views.product,name='product'),
    path('category/<str:foo>',views.category,name='category'),
    path('search/', views.product_search, name='product_search'),
]