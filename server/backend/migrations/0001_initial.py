# Generated by Django 4.1.2 on 2022-10-06 20:50

import ckeditor.fields
from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('weekday', models.IntegerField()),
                ('time', models.TimeField()),
                ('room_number', models.IntegerField()),
                ('teacher_name', models.CharField(max_length=255)),
                ('schedule_type', models.IntegerField(choices=[(0, 'Полный'), (1, 'н/ч'), (2, 'ч/ч')], default=0)),
            ],
            options={
                'ordering': ['weekday', 'time'],
            },
        ),
        migrations.CreateModel(
            name='Template',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.IntegerField(choices=[(1, 'Message'), (2, 'Key'), (3, 'Smile')])),
                ('title', models.CharField(max_length=255)),
                ('body', ckeditor.fields.RichTextField()),
            ],
            options={
                'verbose_name': 'Шаблон',
                'verbose_name_plural': 'Шаблоны',
            },
            managers=[
                ('templates', django.db.models.manager.Manager()),
            ],
        ),
    ]
