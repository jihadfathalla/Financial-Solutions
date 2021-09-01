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
        return Response(data,status=status.HTTP_500_INTERNAL_SERVER_ERROR)    




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
        return Response(data,status=status.HTTP_500_INTERNAL_SERVER_ERROR)    



@api_view(['POST',])
@permission_classes([IsAuthenticated])
def create_question(request):
     """
     Purpose: create new question  obj in Qusetion model,
     param : request,
     """
     if request.method == 'POST':
        question_serializer = QuestionSerializer(data=request.data)
        if question_serializer.is_valid():
               question_serializer.save()
               data = {"success": True ,"data": question_serializer.data}
               return Response(data, status=status.HTTP_200_OK)  
        else:
            data = {"success": False ,"error":question_serializer.errors}
            return Response(data,status=status.HTTP_204_NO_CONTENT)




@api_view(['POST',])
@permission_classes([IsAuthenticated])
def create_answer(request):
    """
    Purpose: create new answer  obj in Answer model,
    param : request,
    """
    if request.method == 'POST':
        answer_serializer = AnswerSerializer(data=request.data)
        if answer_serializer.is_valid():
               answer_serializer.save()
               data = {"success": True ,"data": answer_serializer.data}
               return Response(data, status=status.HTTP_200_OK)  
        else:
            data = {"success": False ,"error":Answer_serializer.errors}
            return Response(data,status=status.HTTP_204_NO_CONTENT)

@api_view(['POST',])
@permission_classes([IsAuthenticated])
def create_section(request):
    """
    Purpose: create new section  obj in Section model,
    param : request,
    """
    if request.method == 'POST':
        section_serializer = SectionSerializer(data=request.data)
        if section_serializer.is_valid():
               section_serializer.save()
               data = {"success": True ,"data": section_serializer.data}
               return Response(data, status=status.HTTP_200_OK)  
        else:
            data = {"success": False ,"error":section_serializer.errors}
            return Response(data,status=status.HTTP_204_NO_CONTENT)
