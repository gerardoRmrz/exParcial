# Generated by Django 4.1 on 2024-08-18 21:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tema',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreTema', models.CharField(blank=True, max_length=48, null=True)),
                ('descripcionTema', models.CharField(blank=True, max_length=256, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Articulo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreArticulo', models.CharField(blank=True, max_length=48, null=True)),
                ('contenidoArticulo', models.CharField(blank=True, max_length=256, null=True)),
                ('temaRelacionado', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='wikiApp.tema')),
            ],
        ),
    ]
