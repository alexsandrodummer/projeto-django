# Generated by Django 5.0.7 on 2024-08-31 22:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='car',
            old_name='models_year',
            new_name='model_year',
        ),
    ]
