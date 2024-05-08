from django.db import models

class Contactform(models.Model):
    Name = models.CharField(max_length=50)
    Company=models.CharField(max_length=50)
    Email = models.EmailField(max_length=50)
    # pwd = models.CharField(max_length=50)
    Subject = models.TextField(max_length=225)
    def __str__(self):
        return self.Email

