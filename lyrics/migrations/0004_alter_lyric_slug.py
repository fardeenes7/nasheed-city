# Generated by Django 3.2.8 on 2021-11-02 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lyrics', '0003_lyric_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lyric',
            name='slug',
            field=models.SlugField(max_length=255),
        ),
    ]