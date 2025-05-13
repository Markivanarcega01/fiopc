from django.urls import path
from . import views

app_name = 'services'
urlpatterns = [
    path('',views.index, name='index'),
    path('consulting-services/',views.display_consulting_services, name='consulting-services'),
    path('rehabilitation/',views.display_rehabilitation, name='rehabilitation'),
    path('technology-upgrade/',views.display_technology_upgrade, name='technology-upgrade'),
    path('engineering-services/',views.display_engineering_services, name='engineering-services'),
    path('operations-and-maintenance/',views.display_operations_and_maintenance, name='operations-and-maintenance'),
    path('design-and-build/',views.display_design_and_build, name='design-and-build'),
]