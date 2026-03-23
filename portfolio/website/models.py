from django.db import models

# Create your models here.
class contact(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email=models.EmailField()
    company=models.CharField(max_length=100)
    Project_type=models.CharField(max_length=100,blank=True)
    budget=models.CharField(max_length=100,blank=True)
    message=models.TextField()

    def __str__(self):
        return self.first_name