from django.contrib import admin
from django.urls import path
from .import views
#funcation  based 

urlpatterns = [
    path('func/', views.myview, name ='func'),
    path('class/',views.MyView.as_view(), name ='class'),
    path('child/',views.MyViewchild.as_view(),name ='child'),
    
]