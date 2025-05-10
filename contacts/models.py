from django.db import models

class ContactMessage(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    company = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    message = models.TextField(blank=True, null=True)
    contact_num = models.CharField(max_length=20)

    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.email}"
