from django.urls import path
from loopstudy import views


urlpatterns = [
    path('', views.index, name='index'),
    path('perfil/',views.perfil, name='perfil'),
    path('ciclos/', views.CicloListView.as_view(), name='ciclos'),
     path('ciclo/<int:pk>', views.CicloDetailView.as_view(), name='ciclo-detail'),
    
]