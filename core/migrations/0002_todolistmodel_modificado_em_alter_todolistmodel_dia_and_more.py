# Generated by Django 4.2.1 on 2023-05-06 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todolistmodel',
            name='modificado_em',
            field=models.DateTimeField(auto_now=True, verbose_name='modificado em'),
        ),
        migrations.AlterField(
            model_name='todolistmodel',
            name='dia',
            field=models.IntegerField(verbose_name='Data'),
        ),
        migrations.AlterField(
            model_name='todolistmodel',
            name='nome',
            field=models.CharField(max_length=80, verbose_name='Tarefa'),
        ),
    ]