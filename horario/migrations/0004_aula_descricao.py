# Generated by Django 5.1.4 on 2025-03-04 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('horario', '0003_remove_aula_fim'),
    ]

    operations = [
        migrations.AddField(
            model_name='aula',
            name='descricao',
            field=models.CharField(default='', max_length=255),
        ),
    ]
