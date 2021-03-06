# Generated by Django 3.2.8 on 2021-11-01 15:47

import ckeditor.fields
import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('display_name', models.TextField(max_length=20)),
                ('facebook', models.TextField(null=True)),
                ('youtube', models.TextField(null=True)),
                ('profile_picture', models.ImageField(upload_to='')),
                ('bio', models.TextField(max_length=200, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Lyric',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=100)),
                ('singer', models.TextField(default='Unknown', max_length=20)),
                ('lyrics', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('youtube_link', models.TextField(max_length=200)),
                ('language', models.CharField(choices=[('Arabic', 'Arabic'), ('Bangla', 'Bangla'), ('English', 'English'), ('Urdu', 'Urdu'), ('Mixed', 'Mixed'), ('Other', 'Other')], default='Other', max_length=10)),
                ('date', models.DateField(default=datetime.datetime.today)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lyrics.profile')),
            ],
        ),
    ]
