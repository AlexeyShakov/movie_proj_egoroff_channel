# Generated by Django 4.0.6 on 2022-07-28 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0002_movie_budjet_movie_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='slug',
            field=models.SlugField(default='', null=True),
        ),
    ]
