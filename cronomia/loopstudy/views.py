from django.shortcuts import render
from loopstudy.models import Cor, Ciclo, Disciplina, TipoDisciplina, Profile, Sprint
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
def index(request):
    context = {}
    return render(request,'index.html', context=context)

def perfil(request):
    #Fazer função depois de fazer o Login
    context = {}
    return render(request,'perfil.html', context=context)


class CicloListView(LoginRequiredMixin, generic.ListView):
    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'    
    model = Ciclo
    
    def get_queryset(self):
        return Ciclo.objects.filter(dono=Profile.objects.filter(user=self.request.user)[0])
    #alterar queryset depois do sistema de login para retornar apenas os ciclos do usuário

class CicloDetailView(LoginRequiredMixin, generic.DetailView):
    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'    
    model = Ciclo

#Forms
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

class CicloCreate(LoginRequiredMixin, CreateView):
    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'    
    model = Ciclo
    
    fields = ['nome','descricao']
    success_url = reverse_lazy('ciclos')

    def form_valid(self, form):
        form.instance.dono = Profile.objects.filter(user=self.request.user)[0]
        return super().form_valid(form)    

class CicloUpdate(LoginRequiredMixin, UpdateView):
    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'    
    model = Ciclo
    fields = ['nome','descricao']
    success_url = reverse_lazy('ciclos')

class CicloDelete(LoginRequiredMixin, DeleteView):
    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'    
    model = Ciclo
    success_url = reverse_lazy('ciclos')
    #disciplinas = Disciplina.objects.filter(ciclo = Ciclo.id)
