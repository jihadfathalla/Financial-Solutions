from django.urls import path, include
from business_plane import views


app_name= 'business_plane'

urlpatterns =[
     ######################### patient URLs ###################################
     path('create/business_plane', views.create_business_plane, name='create-business-plane'),
     path('create/business_plane_information', views.create_business_plane_information, name='create-business-plane-information'),
     path('list/answers', views.list_answers_for_business_plane, name='list-answers'),




]