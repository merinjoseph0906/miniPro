# Generated by Django 4.1 on 2023-02-24 09:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0024_book_add_status_alter_feedbacks_dob_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='bloodgroup',
            field=models.CharField(choices=[('A+', 'A-'), ('B+', 'B-'), ('AB+', 'AB-'), ('O+', 'O-')], default='None', max_length=50),
        ),
        migrations.AddField(
            model_name='account',
            name='childname',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='account',
            name='dob',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='account',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('others', 'others'), ('None', 'None')], default='None', max_length=50),
        ),
        migrations.AddField(
            model_name='account',
            name='weight',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='feedbacks',
            name='dob',
            field=models.DateField(default=datetime.date(2023, 2, 24)),
        ),
        migrations.AlterField(
            model_name='update_profile',
            name='dob',
            field=models.DateField(default=datetime.date(2023, 2, 24)),
        ),
        migrations.AlterField(
            model_name='userprofile_update',
            name='dob',
            field=models.DateField(default=datetime.date(2023, 2, 24)),
        ),
    ]
