from django.http import JsonResponse
from django.urls import reverse
from .models import Application, JobOpportunity
from django.shortcuts import redirect, render
from django.contrib import messages

def index(request):
    try:
        jobs = JobOpportunity.objects.all()
    except:
        return JsonResponse({'error': 'Something went wrong'})
    return render(request, 'careers/careers.html', {'jobs': jobs})

def create_application(request):
    try:
        if request.method == 'POST':
            full_name = request.POST.get('full_name')
            email = request.POST.get('email')
            additional_info = request.POST.get('additional_info')
            cv_file = request.FILES.get('cv')
            job_id = request.POST.get('job_id')

            job = JobOpportunity.objects.get(id=job_id)

            Application.objects.create(
                full_name=full_name,
                email=email,
                additional_info=additional_info,
                cv=cv_file,
                job=job
            )
            messages.success(request, 'Application submitted successfully')
            #return render(request, 'careers/careers.html', {'success': True, })
        return redirect(reverse('careers:index'), success=True)
    except:
        return JsonResponse({'error': 'Something went wrong'})
    