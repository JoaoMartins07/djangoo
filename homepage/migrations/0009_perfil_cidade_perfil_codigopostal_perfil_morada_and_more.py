# Generated by Django 5.1.4 on 2025-03-02 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0008_rename_telefone_perfil_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfil',
            name='cidade',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='perfil',
            name='codigopostal',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='perfil',
            name='morada',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='perfil',
            name='telemovel',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
