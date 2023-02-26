# Generated by Django 4.1 on 2023-02-23 18:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0023_rename_hospital_name_add_hospitaldetails_hosp_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='book_add',
            name='status',
            field=models.CharField(default='000000', max_length=200),
        ),
        migrations.AlterField(
            model_name='feedbacks',
            name='dob',
            field=models.DateField(default=datetime.date(2023, 2, 23)),
        ),
        migrations.AlterField(
            model_name='update_profile',
            name='dob',
            field=models.DateField(default=datetime.date(2023, 2, 23)),
        ),
        migrations.AlterField(
            model_name='userprofile_update',
            name='dob',
            field=models.DateField(default=datetime.date(2023, 2, 23)),
        ),
    ]