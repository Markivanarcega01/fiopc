from django.urls import path
from . import views

app_name = 'major_clients'
urlpatterns = [
    path('',views.index, name='index'),
]