from django.db.models import fields
from rest_framework import serializers
from .models import *
from rest_framework.fields import CurrentUserDefault
from rest_framework.exceptions import APIException








class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields='__all__'


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields='__all__'


class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields='__all__'
