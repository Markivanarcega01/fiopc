from django.shortcuts import render, redirect
from .models import ContactMessage
from django.contrib import messages
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
            messages.success(request, 'Message submitted successfully')
            return render(request, "contacts/contacts.html", {"isSuccess": True})
            #return redirect(reverse('contacts:index'), success=True)
        else:
            return render(request, "contacts/contacts.html", {"isSuccess": False})
    except Exception as e:
        print("Error:", e)
        return JsonResponse({'error': 'Something went wrong'})
