from django.db import models
from django.contrib.auth.models import User
from section.models import Section


# Create your models here.

class BusinessPlane(models.Model):
    user =models.ForeignKey(User,on_delete=models.CASCADE,blank=True, null=True)
    section =models.ForeignKey(Section,on_delete=models.CASCADE,blank=True, null=True)
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.user.username + self.name