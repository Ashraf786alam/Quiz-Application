# Generated by Django 3.1.2 on 2020-12-06 05:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0012_mark_chemistry'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mark',
            old_name='Chemistry',
            new_name='chemistry',
        ),
    ]
