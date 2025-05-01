from .models import Application, JobOpportunity
from django.shortcuts import render

def index(request):
    jobs = JobOpportunity.objects.all()
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

        return render(request, 'careers/careers.html', {'success': True, 'jobs': jobs})

    return render(request, 'careers/careers.html', {'jobs': jobs})
