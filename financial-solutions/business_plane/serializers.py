from django.db.models import fields
from rest_framework import serializers
from .models import *
from rest_framework.fields import CurrentUserDefault
from rest_framework.exceptions import APIException
from rest_framework import status
from rest_framework.response import Response








class ValidationError406(APIException):
        status_code = status.HTTP_406_NOT_ACCEPTABLE



class BusinessPlaneSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessPlane
        exclude =('user',)
    def create(self, validated_data):
        user = self.context.get('user')
        business_plane_obj = BusinessPlane(**validated_data)
        business_plane_obj.user = user
        try:
            business_plane_obj.save()
        except  Exception as e:
            print(e)
            raise ValidationError406(detail ={"response_id": HTTP_500_INTERNAL_SERVER_ERROR,"error": "Can not create  Business Plane, Please contact your system administrator."})
        return  business_plane_obj   
    
    def update(self ,instance, validated_data,*args ,**kwargs):
        user = self.context.get('user')
        instance.user = user
        instance.name = validated_data.get('name',instance.name)
        try:
            instance.save()
        except  Exception as e:
            print(e)
            raise ValidationError406(detail ={"response_id": HTTP_500_INTERNAL_SERVER_ERROR,"error": "Can not create  Business Plane, Please contact your system administrator."})
        return instance

        
         

class BusinessPlaneInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessPlaneInformation
        fields = '__all__'
    def create(self, validated_data):
        business_plane = self.context.get('business_plane')
        business_plane_information_obj = BusinessPlaneInformation(**validated_data)
        business_plane_information_obj.business_plane = business_plane
        try:
            business_plane_information_obj.save()
        except  Exception as e:
            print(e)
            raise ValidationError406(detail ={"response_id": HTTP_500_INTERNAL_SERVER_ERROR,"error": "Can not create  Business Plane information, Please contact your system administrator."})
        return business_plane_information_obj


    def update(self ,instance, validated_data,*args ,**kwargs):
        business_plane = self.context.get('business_plane')
        instance.business_plane = business_plane
        instance.question = validated_data.get('question',instance.question)
        instance.answer = validated_data.get('answer',instance.answer)
        try:
            instance.save()
        except  Exception as e:
            print(e)
            raise ValidationError406(detail ={"response_id": HTTP_500_INTERNAL_SERVER_ERROR,"error": "Can not create  Business Plane information, Please contact your system administrator."})
        return instance    
    
