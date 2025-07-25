"""
URL configuration for fi_opc project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', include('products.urls')),
    path('careers/', include('careers.urls')),
    path('contacts/', include('contacts.urls')),
    path('services/', include('services.urls')),
    path('licenses-certificates/', include('licenses_certificates.urls')),
    path('', include('home.urls')),
    path('partners/', include('partners.urls')),
    path('about/', include('about.urls')),
    path('major-clients/', include('major_clients.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
