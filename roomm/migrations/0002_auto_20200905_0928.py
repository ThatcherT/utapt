# Generated by Django 3.1 on 2020-09-05 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roomm', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roommateprofile',
            name='school',
            field=models.CharField(choices=[('E', 'Cockrell School of Engineering'), ('L', 'School of Liberal Arts'), ('M', 'Mccombs School of Business'), ('N', 'School of Natural Sciences')], max_length=1),
        ),
    ]
