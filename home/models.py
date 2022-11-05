
from distutils.command.upload import upload
from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager,PermissionsMixin
import datetime
import datetime

# Create your models here.
# class Childreg(models.Model):
#     username=models.CharField(max_length=250,unique=True)
#     password=models.CharField(max_length=250,blank=True)
#     confirm_password=models.CharField(max_length=250,blank=True)
#     name=models.CharField(max_length=250,blank=True)

#     class Meta:
#         ordering=('name',)
#         verbose_name='childreg'
#         verbose_name_plural='childreg'

#     def __str__(self):
#         return '{}'.format(self.name)


# class tbl_hospitalregis(models.Model):
#     usertype=models.CharField(max_length=20)
#     username=models.CharField(max_length=30)
#     email=models.CharField(max_length=50)
#     password=models.CharField(max_length=50)
#     location=models.CharField(max_length=50)
#     phonenumber=models.BigIntegerField()
    

#     def __str__(self):
#         return self.f_name

class MyAccountManager(BaseUserManager):
    def create_user(self,username,phonenumber,email,address,city,pincode,district,is_child,is_ashaworker,is_hospital,is_PHC,password=None):
        
        if not email:
            raise ValueError('User must have an email address')

        if not username:
            raise ValueError('User must have an username')

        user = self.model(
            email = self.normalize_email(email),
            username = username,
            phonenumber = phonenumber,
            address = address,
            city = city,
            pincode = pincode,
            district = district,
            is_child=is_child,
            is_ashaworker=is_ashaworker,
            is_hospital=is_hospital,
            is_PHC=is_PHC

        )

        user.set_password(password)
        user.save(using=self._db)
        return user


# class MyAccountManager(BaseUserManager):
#     def create_user(self,username, email, password=None):
#         if not email:
#             raise ValueError('User must have an email address')

#         if not username:
#             raise ValueError('User must have an username')

#         user = self.model(
#             email = self.normalize_email(email),
#             username = username,
            
#         )

#         user.set_password(password)
#         user.save(using=self._db)
#         return user


    
    def create_superuser(self,username,password,email,**extra_fields):
        user = self.create_user(
            email = self.normalize_email(email),
            username = username,
            password = password, **extra_fields
            # first_name = first_name,
            # last_name = last_name,
        )
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True
        user.save(using=self._db)
        return user


 
class Account(AbstractBaseUser,PermissionsMixin):
    status_choices=(('Approved','Approved'),('Pending','Pending'), ('None','None'))
    role_choices=(('is_admin','is_admin'),('is_child','is_child'),('is_ashaworker','is_ashaworker'),('is_hospital','is_hospital'),('is_PHC','is_PHC'))
    district_choices=(
        ('Kozhikode','Kozhikode'),
        ('Malappuram','Malappuram'),
        ('Kannur','Kannur'),
        # ('Trivandrum','Trivandrum'),
        ('Palakkad','Palakkad'),
        ('Thrissur','Thrissur'),
        ('Kottayam','Kottayam'),
        ('Alappuzha','Alappuzha'),
        ('Idukki','Idukki'),
        ('Kollam','Kollam'),
        ('Ernakulam','Ernakulam'),
        ('Wayanad','Wayanad'),
        ('Kasaragod','Kasaragod'),
        ('Pathanamthitta','Pathanamthitta'),
        ('Thiruvananthapuram','Thiruvananthapuram'),
        ('None','None'),
    )


    id            = models.AutoField(primary_key=True)
    username      = models.CharField(max_length=100, default='')
    phonenumber   = models.BigIntegerField(default=0)
    email         = models.EmailField(max_length=100, unique=True)
    address       = models.CharField(max_length=100, default='')
    city          = models.CharField(max_length=100, default='')
    pincode       = models.BigIntegerField(default=0)
    district      = models.CharField(max_length=50,choices=district_choices,default='None')
    role          = models.CharField(max_length=100,choices=role_choices)

    # required
    date_joined     = models.DateTimeField(auto_now_add=True)
    last_login      = models.DateTimeField(auto_now_add=True)
    is_admin        = models.BooleanField(default=False)
    is_child      = models.BooleanField(default=False)
    is_ashaworker  = models.BooleanField(default=False)
    
    is_hospital      = models.BooleanField(default=False)
    is_PHC        = models.BooleanField(default=False)

    
    is_active       = models.BooleanField(default=True)
    is_superadmin   = models.BooleanField(default=False)
    is_staff      = models.BooleanField(default=False) 
    #is_ashaworker      = models.BooleanField(default=False)
    is_superadmin     = models.BooleanField(default=False)  
   

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','phonenumber', 'address','city','pincode','district','is_child','is_ashaworker','is_hospital','is_PHC']
    # REQUIRED_FIELDS = [,'password']



    objects = MyAccountManager()

    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, add_label):
        return True

class tbl_addprofile(models.Model):
    fathersname=models.CharField(max_length=20)
    mothersname=models.CharField(max_length=30)
    panchayath=models.CharField(max_length=50)
    location=models.CharField(max_length=50)
    weight=models.BigIntegerField()
    dob=models.DateField(default=0)
    

    def __str__(self):
        return self.f_name
class addvaccine(models.Model):
    # vaccine_id=models.AutoField(primary_key=True)
    vaccinename = models.CharField(max_length=100)
    disease = models.CharField(max_length=100)
    age = models.CharField(max_length=100)
    
    def __str__(self):
         return self.vaccinename
        
# class addvaccinedate(models.Model):
#     vaccinename = models.ForeignKey(addvaccine, on_delete=models.CASCADE, default=1)
#     vaccinedate = models.DateField(default=0)
#     vaccinetime = models.CharField(max_length=200)
   
#     def __str__(self):
#           return self.vaccinename
class vaccinedate(models.Model):
    vaccinename = models.ForeignKey(addvaccine, on_delete=models.CASCADE, default=1)
    vaccinedate = models.DateField(default=0)
    vaccinetime = models.CharField(max_length=200)