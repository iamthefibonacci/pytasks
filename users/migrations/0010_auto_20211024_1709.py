# Generated by Django 3.2.8 on 2021-10-24 17:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_auto_20211024_1548'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='address_file',
            new_name='address_image',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='id_file',
            new_name='id_image',
        ),
    ]