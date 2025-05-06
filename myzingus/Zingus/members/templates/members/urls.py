from django.urls import path
from . import views
from . import login

urlpatterns = [
   	path('', views.main, name='main'),
   	path('zinguses/', views.members, name='zinguses'),
  	path('zinguses/search/details/<int:id>', views.details, name='details'),
  	path('testing/', views.testing, name='testing'),    
  	path('login/', views.login, name='login'),
	path('cool/', views.cool, name='cool'),
	path('zinguses/add/', views.add, name='add'),
	path('zinguses/add/addrecord/', views.addrecord, name='addrecord'),
	path('zinguses/search/', views.search, name='search'),
]