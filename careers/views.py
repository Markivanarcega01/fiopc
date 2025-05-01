from django.shortcuts import render, redirect
from .models import Application

def index(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        additional_info = request.POST.get('additional_info')
        cv_file = request.FILES.get('cv')

        Application.objects.create(
            full_name=full_name,
            email=email,
            additional_info=additional_info,
            cv=cv_file
        )

        return render(request, 'careers/careers.html', {'success': True})

    return render(request, 'careers/careers.html')
