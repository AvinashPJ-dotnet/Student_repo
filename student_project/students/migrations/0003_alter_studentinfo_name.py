# Generated by Django 3.2.10 on 2022-01-11 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_auto_20220111_1054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentinfo',
            name='name',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]