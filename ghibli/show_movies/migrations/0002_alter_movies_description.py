# Generated by Django 3.2.3 on 2021-05-20 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('show_movies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movies',
            name='description',
            field=models.TextField(),
        ),
    ]
