from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('confirm/<str:name>/<int:size>/<str:encoding>', views.confirm),
]
