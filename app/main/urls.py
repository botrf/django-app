from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home' ),
    path('about-as', views.about, name='about'),
    path('create-task', views.create_task, name='create')

]
