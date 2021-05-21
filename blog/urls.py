from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('finish/',views.ordered,name='blog-finish'),
    path('cart/', views.cart, name='blog-cart'),
    path('orders/', views.orders, name='blog-orders'),
    path('about/', views.about, name='blog-about'),
    path('lev1/',views.level1,name='blog-level1'),
    path('lev2/',views.level2,name='blog-level2'),
    path('lev3/',views.level3,name='blog-level3'),
    path('lev4/',views.level4,name='blog-level4'),
    path('help/',views.help,name='blog-help'),

]