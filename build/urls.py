from django.contrib import admin
from django.urls import path
from . import views

app_name = 'build'
urlpatterns = [
    path('', views.home),
    path('career_details', views.career_details),
    path('education', views.education),
    path('skills', views.skills),
    path('summary', views.summary),
    path('contact_details', views.contact),
    path('design_select', views.design_select),
    path('submit_details1', views.submit_details1),
    path('submit_details2', views.submit_details2),
    path('features', views.features)
]
