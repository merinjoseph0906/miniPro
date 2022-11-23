# Generated by Django 4.1 on 2022-11-20 05:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_delete_booking'),
    ]

    operations = [
        migrations.CreateModel(
            name='booking_add',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vaccination_date', models.DateField(blank=True, null=True)),
                ('vaccine_name', models.CharField(max_length=200)),
                ('child_name', models.CharField(max_length=200)),
                ('dose', models.BigIntegerField()),
                ('hospital_name', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='home.new_stock')),
                ('time_slot', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='home.add_timeslot')),
            ],
        ),
    ]