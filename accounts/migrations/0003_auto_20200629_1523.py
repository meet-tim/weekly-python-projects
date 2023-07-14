# Generated by Django 3.0.2 on 2020-06-29 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_house'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Customer',
            new_name='Owner',
        ),
        migrations.AlterField(
            model_name='house',
            name='property_type',
            field=models.CharField(choices=[('Sale', 'Sale'), ('Rent', 'Rent')], max_length=100),
        ),
    ]
