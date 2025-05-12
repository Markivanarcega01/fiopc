from django.urls import path
from . import views

app_name = 'contacts'
urlpatterns = [
     path('', views.index, name='index'),
     path('create_message/', views.create_message, name='create_message'),
]
