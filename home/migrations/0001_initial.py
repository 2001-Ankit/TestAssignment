# Generated by Django 5.0.6 on 2024-05-14 08:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=400)),
                ('description', models.TextField()),
                ('slug', models.SlugField(blank=True, max_length=400)),
                ('category', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='home.category')),
            ],
        ),
    ]
