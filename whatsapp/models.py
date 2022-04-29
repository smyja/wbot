from django.db import models
from phone_field import PhoneField

# Create your models here.
class Log(models.Model):
    message = models.CharField(max_length=256)
    phone_number = models.CharField(max_length=256)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return  f"{self.phone_number}-{self.created_at}"