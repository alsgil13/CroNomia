# Generated by Django 2.2.7 on 2019-12-16 12:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ciclo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(help_text='Nome do seu ciclo de estudos (e.g. Vestibular, Concurso, POSCOMP...)', max_length=50)),
                ('descricao', models.TextField(verbose_name='Descrição')),
                ('dt_cria', models.DateTimeField(auto_now=True)),
                ('tamanho', models.IntegerField()),
                ('laps', models.IntegerField(help_text='Quantidade de vezes que o ciclo foi estudado')),
            ],
        ),
        migrations.CreateModel(
            name='Cor',
            fields=[
                ('code', models.CharField(max_length=8, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Disciplina',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(help_text='Nome da Disciplina', max_length=50)),
                ('familiaridade', models.IntegerField()),
                ('tempo', models.IntegerField()),
                ('ciclo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loopstudy.Ciclo')),
                ('cor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='loopstudy.Cor')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='profile', serialize=False, to=settings.AUTH_USER_MODEL)),
                ('dt_nasc', models.DateField(blank=True, null=True, verbose_name='Data de Nascimento')),
                ('cep', models.CharField(help_text='Digite o CEP do seu endereço', max_length=8)),
                ('cidade', models.CharField(max_length=200)),
                ('estado', models.CharField(max_length=2)),
                ('pais', models.CharField(max_length=50)),
                ('foto', models.ImageField(default='profile_pics/no-image-icon.png', upload_to='profile_pics')),
            ],
        ),
        migrations.CreateModel(
            name='TipoDisciplina',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(help_text='Nome do Tipo (e.g. Teórica, Prática, Treinamento Físico)', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Sprint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ini', models.DateTimeField(verbose_name='Início')),
                ('fim', models.DateTimeField()),
                ('done', models.BooleanField(default=False)),
                ('disc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loopstudy.Disciplina')),
                ('usr', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loopstudy.Profile')),
            ],
        ),
        migrations.AddField(
            model_name='disciplina',
            name='tipo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='loopstudy.TipoDisciplina'),
        ),
    ]
