from django.urls import path
from loopstudy import views


urlpatterns = [
    path('', views.index, name='index'),
]