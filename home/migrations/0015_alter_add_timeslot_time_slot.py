# Generated by Django 4.1 on 2022-11-23 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_remove_add_vaccines_side_effects'),
    ]

    operations = [
        migrations.AlterField(
            model_name='add_timeslot',
            name='time_slot',
            field=models.TimeField(max_length=200),
        ),
    ]