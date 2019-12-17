from django.shortcuts import render
from loopstudy.models import Cor, Ciclo, Disciplina, TipoDisciplina, Profile, Sprint
from django.views import generic

# Create your views here.
def index(request):
    context = {}
    return render(request,'index.html', context=context)

def perfil(request):
    #Fazer função depois de fazer o Login
    context = {}
    return render(request,'perfil.html', context=context)

class CicloListView(generic.ListView):
    model = Ciclo
    #alterar queryset depois do sistema de login para retornar apenas os ciclos do usuário

class CicloDetailView(generic.DetailView):
    model = Ciclo
    
    

    #disciplinas = Disciplina.objects.filter(ciclo = Ciclo.id)
