# Generated by Django 3.1.2 on 2020-12-05 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0010_auto_20201205_1614'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mark',
            name='biology',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='mark',
            name='english',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='mark',
            name='math',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='mark',
            name='physics',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='mark',
            name='social',
            field=models.IntegerField(default=0),
        ),
    ]
