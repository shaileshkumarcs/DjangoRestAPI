from django.db import models


# Create your models here.

class Btech(models.Model):
    first_name = models.CharField(max_length=128, blank=False, null=False)
    last_name = models.CharField(max_length=128)
    email = models.EmailField(max_length=128, blank=False, null=False)
    rollno = models.CharField(max_length=10, blank=False, null=False)


