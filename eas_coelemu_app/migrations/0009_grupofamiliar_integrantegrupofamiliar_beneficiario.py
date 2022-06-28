# Generated by Django 4.0.4 on 2022-06-25 04:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eas_coelemu_app', '0008_rename_cantidad_canvenios_cantidadconvenio_cantidad_convenios'),
    ]

    operations = [
        migrations.CreateModel(
            name='GrupoFamiliar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('calif_soc_eco', models.IntegerField()),
                ('direccion', models.CharField(max_length=200)),
                ('rhs_archivo', models.FileField(blank=True, null=True, upload_to='grupo_familiar/')),
                ('estado', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='IntegranteGrupoFamiliar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=255)),
                ('apellido_paterno', models.CharField(max_length=255)),
                ('apellido_materno', models.CharField(max_length=255)),
                ('rut', models.IntegerField()),
                ('dv', models.CharField(max_length=1)),
                ('parentesco', models.CharField(max_length=25)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('grupo_familiar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='integrante', to='eas_coelemu_app.grupofamiliar')),
            ],
        ),
        migrations.CreateModel(
            name='Beneficiario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('grupo_familiar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='beneficiario', to='eas_coelemu_app.grupofamiliar')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='beneficiario', to='eas_coelemu_app.usuario')),
            ],
        ),
    ]