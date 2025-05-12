from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "services/services.html")

def display_consulting_services(request):
    return render(request, "services/consulting_services.html")

def display_engineering_services(request):
    return render(request, "services/engineering_services.html")

def display_rehabilitation(request):
    return render(request, "services/rehabilitation.html")

def display_technology_upgrade(request):
    return render(request, "services/technology_upgrade.html")