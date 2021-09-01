from django.db import models
from django.contrib.auth.models import User
from section.models import Question ,Answer


# Create your models here.

class BusinessPlane(models.Model):
    user =models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.user.username + self.name



class BusinessPlaneInformation(models.Model):
    business_plane =models.ForeignKey(BusinessPlane,on_delete=models.CASCADE)
    question =models.ForeignKey(Question,on_delete=models.CASCADE)
    answer =models.ForeignKey(Answer,on_delete=models.CASCADE)

    def __str__(self):
        return self.business_plane.name