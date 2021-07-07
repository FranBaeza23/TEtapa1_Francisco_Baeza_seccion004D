# Generated by Django 3.2.3 on 2021-07-07 20:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datos',
            name='email',
            field=models.CharField(max_length=50, verbose_name='Email'),
        ),
        migrations.CreateModel(
            name='publicacion',
            fields=[
                ('email', models.CharField(max_length=100, primary_key=True, serialize=False, verbose_name='Correo')),
                ('nombre', models.CharField(max_length=30, verbose_name='Nombre')),
                ('detalles', models.CharField(max_length=150, verbose_name='Detalles')),
                ('rutcola', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.datos')),
            ],
        ),
    ]