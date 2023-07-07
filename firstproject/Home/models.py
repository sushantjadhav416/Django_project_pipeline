from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    password = models.CharField(max_length=20)
    password2 = models.CharField(max_length=20)
    phone = models.CharField(max_length=12)
    
    

   

