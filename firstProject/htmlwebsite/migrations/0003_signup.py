# Generated by Django 5.0.2 on 2024-03-27 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('htmlwebsite', '0002_loginform'),
    ]

    operations = [
        migrations.CreateModel(
            name='Signup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password1', models.CharField(max_length=100)),
                ('password2', models.CharField(max_length=100)),
            ],
        ),
    ]
