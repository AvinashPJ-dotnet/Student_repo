# Generated by Django 3.2.10 on 2022-01-11 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentacademics',
            name='biology',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='studentacademics',
            name='chemistry',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='studentacademics',
            name='english',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='studentacademics',
            name='maths',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='studentacademics',
            name='physics',
            field=models.IntegerField(),
        ),
    ]
