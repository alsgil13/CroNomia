# Generated by Django 2.2.7 on 2019-12-17 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loopstudy', '0004_auto_20191217_1547'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ciclo',
            name='laps',
            field=models.IntegerField(blank=True, help_text='Quantidade de vezes que o ciclo foi estudado', null=True),
        ),
    ]
