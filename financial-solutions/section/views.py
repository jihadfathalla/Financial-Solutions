from django.shortcuts import render
from rest_framework.decorators import api_view 
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated 
from rest_framework.decorators import api_view , permission_classes
from .models import *
from section.serializers import *
from rest_framework import status

# Create your views here.

@api_view(['POST', ])
@permission_classes([IsAuthenticated])
def get_question_answers(request,question_id):
    try:
        question = Question.objects.get(id=question_id)
        answers = Answer.objects.filter(question=question)
        if answers:
            answers_serializer = AnswerSerializer(answers , many=True)
            data = {"success": True ,"data":answers_serializer.data}
            return Response(data, status=status.HTTP_200_OK)     
        else:
            data = {"success": True,"data": []}
            return Response(data,status=status.HTTP_204_NO_CONTENT)
    except Question.DoesNotExist:
        data = {"success": False, "error": "This question id does not exist"}
        return Response(data,status=status.HTTP_204_NO_CONTENT)
    except:
        data = {"success": False,"error":  "Something went wrong, Please contact your sustem administrator."}
        return Response(data.HTTP_500_INTERNAL_SERVER_ERROR)    


@api_view(['POST', ])
@permission_classes([IsAuthenticated])
def get_section_questions(request,section_id):
    try:
        section = Section.objects.get(id=section_id)
        questions = Question.objects.filter(section=section)
        if questions:
            questions_serializer = QuestionSerializer(questions , many=True)
            data = {"success": True ,"data":questions_serializer.data}
            return Response(data, status=status.HTTP_200_OK)     
        else:
            data = {"success": True,"data": []}
            return Response(data,status=status.HTTP_204_NO_CONTENT)
    except Question.DoesNotExist:
        data = {"success": False, "error": "This section id does not exist"}
        return Response(data,status=status.HTTP_204_NO_CONTENT)
    except:
        data = {"success": False,"error":  "Something went wrong, Please contact your sustem administrator."}
        return Response(data.HTTP_500_INTERNAL_SERVER_ERROR)    



