# Generated by Django 3.1 on 2020-09-02 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sublease',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aptname', models.IntegerField()),
                ('description', models.TextField(max_length=500)),
                ('address', models.CharField(max_length=30)),
                ('price', models.IntegerField()),
                ('rooms', models.IntegerField()),
                ('sqft', models.IntegerField()),
                ('dateposted', models.DateField()),
                ('opento', models.CharField(choices=[('M', 'Males'), ('F', 'Females'), ('E', 'Either')], max_length=1)),
                ('negotiable', models.CharField(choices=[('Y', 'Negotiable'), ('N', 'Non-Negotiable')], max_length=1)),
                ('area', models.CharField(choices=[('W', 'West Campus'), ('N', 'North Campus'), ('R', 'Riverside'), ('O', 'Other')], max_length=1)),
            ],
        ),
    ]
