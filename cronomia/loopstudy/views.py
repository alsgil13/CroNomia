from django.shortcuts import render
from loopstudy.models import Cor, Ciclo, Disciplina, TipoDisciplina, Profile, Sprint

# Create your views here.
def index(request):
    context = {}
    return render(request,'index.html', context=context)