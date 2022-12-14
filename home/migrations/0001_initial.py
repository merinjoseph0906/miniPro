# Generated by Django 4.1 on 2022-11-17 15:47

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='about_vaccine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('disease', models.CharField(max_length=400)),
                ('vaccine', models.CharField(max_length=300)),
                ('disease_spread', models.CharField(max_length=300)),
                ('symptoms', models.CharField(max_length=300)),
                ('complications', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Add_vaccines',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vaccine_name', models.CharField(max_length=100)),
                ('disease', models.CharField(max_length=100)),
                ('age', models.CharField(max_length=100)),
                ('no_dose', models.BigIntegerField()),
                ('side_effects', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='demo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('demoname', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='feed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='feedbacks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('dob', models.DateField(default=datetime.date(2022, 11, 17))),
                ('panchayath', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='tbl_addprofile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fathersname', models.CharField(max_length=20)),
                ('mothersname', models.CharField(max_length=30)),
                ('panchayath', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=50)),
                ('weight', models.BigIntegerField()),
                ('dob', models.DateField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='update_profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('dob', models.DateField(default=datetime.date(2022, 11, 17))),
                ('panchayath', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='userprofile_update',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('dob', models.DateField(default=datetime.date(2022, 11, 17))),
                ('panchayath', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='new_stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hospital_name', models.CharField(max_length=200)),
                ('vaccination_type', models.CharField(max_length=200)),
                ('time_slot', models.CharField(max_length=200)),
                ('available_stock', models.BigIntegerField()),
                ('vaccination_date', models.DateField(default=0)),
                ('vaccine_name', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='home.add_vaccines')),
            ],
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(default='', max_length=100)),
                ('phonenumber', models.BigIntegerField(default=0)),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('address', models.CharField(default='', max_length=100)),
                ('city', models.CharField(default='', max_length=100)),
                ('pincode', models.BigIntegerField(default=0)),
                ('district', models.CharField(choices=[('Kozhikode', 'Kozhikode'), ('Malappuram', 'Malappuram'), ('Kannur', 'Kannur'), ('Palakkad', 'Palakkad'), ('Thrissur', 'Thrissur'), ('Kottayam', 'Kottayam'), ('Alappuzha', 'Alappuzha'), ('Idukki', 'Idukki'), ('Kollam', 'Kollam'), ('Ernakulam', 'Ernakulam'), ('Wayanad', 'Wayanad'), ('Kasaragod', 'Kasaragod'), ('Pathanamthitta', 'Pathanamthitta'), ('Thiruvananthapuram', 'Thiruvananthapuram'), ('None', 'None')], default='None', max_length=50)),
                ('role', models.CharField(choices=[('is_admin', 'is_admin'), ('is_child', 'is_child'), ('is_ashaworker', 'is_ashaworker'), ('is_hospital', 'is_hospital'), ('is_PHC', 'is_PHC')], max_length=100)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('last_login', models.DateTimeField(auto_now_add=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_child', models.BooleanField(default=False)),
                ('is_ashaworker', models.BooleanField(default=False)),
                ('is_hospital', models.BooleanField(default=False)),
                ('is_PHC', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superadmin', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
