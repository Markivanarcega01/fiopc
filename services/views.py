from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "services/services.html")

def display_consulting_services(request):
    return render(request, "services/consulting-services.html")

def display_engineering_services(request):
    return render(request, "services/engineering-services.html")

def display_rehabilitation(request):
    return render(request, "services/rehabilitation.html")

def display_technology_upgrade(request):
    return render(request, "services/technology-upgrade.html")

def display_operations_and_maintenance(request):
    return render(request, "services/operations-and-maintenance.html")

def display_design_and_build(request):
    return render(request, "services/design-and-build.html")