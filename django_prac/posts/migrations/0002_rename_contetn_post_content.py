# Generated by Django 4.2 on 2023-05-22 10:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='contetn',
            new_name='content',
        ),
    ]
