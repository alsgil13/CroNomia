from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Cor(models.Model):
    code = models.CharField(max_length=8, primary_key=True)
    
    def __str__(self):
        """String para representar o objeto."""
        return self.code

class Ciclo(models.Model):
    nome = models.CharField(max_length=50, help_text='Nome do seu ciclo de estudos (e.g. Vestibular, Concurso, POSCOMP...)')
    descricao = models.TextField(verbose_name="Descrição")
    dt_cria = models.DateTimeField(auto_now=True)
    tamanho = models.IntegerField(null=True, blank=True)
    laps = models.IntegerField(help_text='Quantidade de vezes que o ciclo foi estudado',null=True, blank=True)
    dono = models.ForeignKey('Profile', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        """String para representar o objeto."""
        return self.nome
    

class TipoDisciplina(models.Model):
    nome = models.CharField(max_length=50, help_text='Nome do Tipo (e.g. Teórica, Prática, Treinamento Físico)')
    
    def __str__(self):
        """String para representar o objeto."""
        return self.nome


class Disciplina(models.Model):
    nome = models.CharField(max_length=50, help_text='Nome da Disciplina')
    cor = models.ForeignKey('Cor', on_delete=models.SET_NULL, null=True)
    ciclo = models.ForeignKey('Ciclo', on_delete=models.CASCADE)
    familiaridade = models.IntegerField()
    tipo = models.ForeignKey('TipoDisciplina', on_delete=models.SET_NULL, null=True)
    tempo = models.IntegerField()
    ativa = models.BooleanField(default=True)
    def __str__(self):
        """String para representar o objeto."""
        return self.nome

class Profile(models.Model):
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE, primary_key=True)
    dt_nasc = models.DateField("Data de Nascimento",null=True, blank=True)
    cep = models.CharField(max_length=8, help_text='Digite o CEP do seu endereço')
    cidade = models.CharField(max_length=200)
    estado = models.CharField(max_length=2)
    pais = models.CharField(max_length=50)
    foto = models.ImageField(upload_to = 'profile_pics', default = 'profile_pics/no-image-icon.png')
    def __str__(self):
        """String for representing the Model object."""
        return f'{self.user.first_name} {self.user.last_name}'   

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()    

class Sprint(models.Model):
    usr = models.ForeignKey('Profile', on_delete=models.CASCADE)
    disc = models.ForeignKey('Disciplina', on_delete=models.CASCADE)
    ini = models.DateTimeField(verbose_name='Início')
    fim = models.DateTimeField()
    done = models.BooleanField(default=False)
    def __str__(self):
        """String para representar o objeto."""
        return f'{self.usr.user.first_name} - {self.disc.nome}'    
