# Generated by Django 4.1 on 2022-11-23 17:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_remove_book_add_time_slot_delete_add_timeslot'),
    ]

    operations = [
        migrations.CreateModel(
            name='time_slot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hospital_name', models.CharField(default='000000', max_length=200)),
                ('time_slot', models.TimeField(max_length=200)),
                ('vaccination_date', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='home.new_stock')),
                ('vaccine_name', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='home.add_vaccines')),
            ],
        ),
    ]