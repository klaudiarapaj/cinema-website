# Generated by Django 4.0.6 on 2022-07-21 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_remove_movie_id_movie_movie_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='bigimage',
            field=models.URLField(),
        ),
        migrations.AlterField(
            model_name='movie',
            name='image',
            field=models.URLField(),
        ),
    ]
