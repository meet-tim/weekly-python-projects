# Generated by Django 3.0.2 on 2020-07-08 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_house_furnishes'),
    ]

    operations = [
        migrations.AddField(
            model_name='house',
            name='no_of_bathrooms',
            field=models.PositiveIntegerField(default=1),
        ),
    ]