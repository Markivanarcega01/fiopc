from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "major_clients/major_clients.html")