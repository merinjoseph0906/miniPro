# Generated by Django 4.1 on 2023-02-21 08:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0020_add_hospitaldetails_alter_feedbacks_dob_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='add_hospitaldetails',
            old_name='type',
            new_name='hos_type',
        ),
    ]