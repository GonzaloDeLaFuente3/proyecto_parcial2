# Generated by Django 4.1.3 on 2022-11-07 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vianda', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tipo_plato',
            name='descripcion',
            field=models.CharField(max_length=300),
        ),
    ]