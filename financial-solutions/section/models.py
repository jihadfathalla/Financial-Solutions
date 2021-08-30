from django.db import models

# Create your models here.

class Section(models.Model):
    name =models.CharField(max_length=250)
    def __str__(self):
        return self.name



class Question(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name='questions')
    question = models.CharField(max_length=255)

    def __str__(self):
        return self.question

class Answer(models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASCADE, related_name='answers')
    answer = models.CharField(max_length=255)

    def __str__(self):
        return self.question.question + self.answer       