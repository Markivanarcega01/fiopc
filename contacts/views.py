from django.shortcuts import render, redirect
from .models import ContactMessage
from django.contrib import messages as msg
from django.http import JsonResponse
from django.urls import reverse

def create_message(request):
    try:
        if request.method == "POST":
            full_name = request.POST.get("full_name")
            email = request.POST.get("email")
            company = request.POST.get("company")
            position = request.POST.get("position")
            message = request.POST.get("message")
            contact_num = request.POST.get("contact-num")

            ContactMessage.objects.create(
                full_name=full_name,
                email=email,
                company=company,
                position=position,
                message=message,
                contact_num=contact_num,
            )
            msg.success(request, 'Message submitted successfully')
            return redirect(reverse('contacts:index'), success=True)

        return render(request, "contacts/contacts.html")
    except Exception as e:
        print("Error:", e)
        return JsonResponse({'error': 'Something went wrong'})
