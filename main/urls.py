from django.urls import path
from main import views

urlpatterns = [
    path('', views.createpost, name='createpost'),
    path('result', views.result, name='result'),


    ]