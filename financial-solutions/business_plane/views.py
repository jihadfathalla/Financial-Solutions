from django.shortcuts import render
from .serializers import BusinessPlaneSerializer,BusinessPlaneInformationSerializer
from rest_framework import status
from rest_framework.decorators import api_view , permission_classes
from rest_framework.permissions import IsAuthenticated 
from rest_framework.response import Response
from .models import BusinessPlane , BusinessPlaneInformation
from section.models import Answer, Question
from section.serializers import AnswerSerializer


# Create your views here.

@api_view(['POST',])
@permission_classes([IsAuthenticated])
def create_business_plane(request):
     """
     Purpose: create new business plane obj in BusinessPlane model,
     param : request,
     """
     if request.method == 'POST':
          business_plane_serializer = BusinessPlaneSerializer(data=request.data , context={'user':request.user})
          if business_plane_serializer.is_valid():
               business_plane_serializer.save()
               data = {"success": True ,"data": business_plane_serializer.data}
               return Response(data, status=status.HTTP_200_OK)  
          else:
                data = {"success": False ,"error":business_plane_serializer.errors}
                return Response(data,status=status.HTTP_204_NO_CONTENT)



@api_view(['POST',])
@permission_classes([IsAuthenticated])
def create_business_plane_information(request):
     """
     Purpose: create new business plane information obj in BusinessPlaneInformation model,
     param : request,
     """
     if request.method == 'POST':
        business_plane_id= request.data['business_plane']
        business_plane_information_serializer = BusinessPlaneInformationSerializer(data=request.data ,
         context={'business_plane': BusinessPlane.objects.get(id=business_plane_id)})
        if business_plane_information_serializer.is_valid():
               business_plane_information_serializer.save()
               data = {"success": True ,"data": business_plane_information_serializer.data}
               return Response(data, status=status.HTTP_200_OK)  
        else:
            data = {"success": False ,"error":business_plane_information_serializer.errors}
            return Response(data,status=status.HTTP_204_NO_CONTENT)







@api_view(['POST', ])
@permission_classes([IsAuthenticated])
def list_answers_for_business_plane(request): 
    """
    Purpose: list all user answers for business plane ,
    """
    try:
        business_plane_id= request.data['business_plane']
        answers=  BusinessPlaneInformation.objects.filter(business_plane__user = request.user,
                business_plane=business_plane_id).values_list('answer',flat=True)
        all_answers = []  
        if answers:
            for answer in answers:
                obj = Answer.objects.get(id = answer)
                all_answers.append(obj)
            answers_serializer = AnswerSerializer(all_answers , many=True)
            data = {"success": True ,"data":answers_serializer.data}
            return Response(data, status=status.HTTP_200_OK)     

                
        else:
            data = {"success": True,"data": []}
            return Response(data,status=status.HTTP_204_NO_CONTENT)
    
    except Exception as e:
        data = {"success": False,"error":  "no business plane id "}
        return Response(data,status=status.HTTP_500_INTERNAL_SERVER_ERROR) 
    