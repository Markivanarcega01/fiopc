from django.urls import path
from . import views

app_name = 'careers'
urlpatterns = [
    path('',views.index, name='index'),
    path('application/',views.create_application, name='create_application'),
]
