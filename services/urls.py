from django.urls import path
from . import views

app_name = 'services'
urlpatterns = [
    path('',views.index, name='index'),
    path('consulting_services/',views.display_consulting_services, name='consulting_services'),
    path('rehabilitation/',views.display_rehabilitation, name='rehabilitation'),
    path('technology_upgrade/',views.display_technology_upgrade, name='technology_upgrade'),
    path('engineering_services/',views.display_engineering_services, name='engineering_services'),
]