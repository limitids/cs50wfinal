# Generated by Django 4.0.2 on 2022-03-29 21:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leaf', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='resturaunt',
            old_name='creater',
            new_name='creator',
        ),
    ]