from django.urls import path, include
from section import views



app_name= 'section'

urlpatterns =[
     ######################### patient URLs ###################################
     path('get/answers/<int:question_id>', views.get_question_answers, name='get-answers-per-question'),
     path('get/questions/<int:section_id>', views.get_section_questions, name='get-questions-per-section'),

     path('create/question', views.create_question, name='create-question'),
     path('create/answer', views.create_answer, name='create-answer'),
     path('create/section', views.create_section, name='create-section'),



]