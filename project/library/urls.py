from django.urls import path
from . import views

urlpatterns = [
    path('', views.library, name='library'),
    path('upload/', views.upload, name='upload'),
]
