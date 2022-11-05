from django.contrib import admin
from .models import Account,addvaccine,vaccinedate
from django.contrib.auth.models import Group

admin.site.unregister(Group)
admin.site.register(addvaccine)
# admin.site.register(addvaccinedate)
admin.site.register(vaccinedate)




admin.site.register(Account)

# Register your models here.
