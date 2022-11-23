# Generated by Django 4.1 on 2022-11-18 05:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_remove_new_stock_time_slot_alter_feedbacks_dob_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='add_timeslot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_slot', models.CharField(max_length=200)),
                ('vaccination_date', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='home.new_stock')),
                ('vaccine_name', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='home.add_vaccines')),
            ],
        ),
    ]