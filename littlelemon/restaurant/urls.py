from django.contrib import admin 
from django.urls import path 
#from .views import sayHello 
from . import views
  
urlpatterns = [ 
#    path('', sayHello, name='sayHello'),
    path('menu/', views.MenuItemView.as_view()),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
]
