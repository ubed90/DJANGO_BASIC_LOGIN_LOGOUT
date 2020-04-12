from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfileInfo(models.Model):

    user = models.OneToOneField(User , on_delete = models.CASCADE)

    name = models.CharField(max_length = 256)

    DOB = models.CharField(max_length = 100)

    def __str__(self):
        return self.name
