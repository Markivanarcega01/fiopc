from django.db import models

class JobOpportunity(models.Model):
    title = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    description = models.TextField()
    qualifications = models.TextField(blank=True)
    requirements = models.TextField(blank=True)

    def __str__(self):
        return f"{self.company_name} - {self.title}"

class Application(models.Model):
    job = models.ForeignKey(JobOpportunity, on_delete=models.CASCADE, default=None)
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    additional_info = models.TextField(blank=True)
    cv = models.FileField(upload_to='files')

    def __str__(self):
        return f"{self.full_name} - {self.job}"
