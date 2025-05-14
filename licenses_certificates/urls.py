from django.urls import path
from . import views

app_name = 'licenses_certificates'
urlpatterns = [
    path('',views.index, name='index'),
]
