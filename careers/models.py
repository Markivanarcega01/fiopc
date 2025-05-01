from django.db import models

class Application(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    additional_info = models.TextField(blank=True)
    cv = models.FileField(upload_to='cvs/')

    def __str__(self):
        return self.full_name
