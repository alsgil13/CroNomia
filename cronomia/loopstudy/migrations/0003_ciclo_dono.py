# Generated by Django 2.2.7 on 2019-12-17 13:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('loopstudy', '0002_disciplina_ativa'),
    ]

    operations = [
        migrations.AddField(
            model_name='ciclo',
            name='dono',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='loopstudy.Profile'),
        ),
    ]
