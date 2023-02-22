from django.contrib import admin
from .models import Account,Add_vaccines,new_stock,book_add
from django.contrib.auth.models import Group
from django.http import HttpResponse
import csv

admin.site.unregister(Group)
# admin.site.register(new_stock)
# admin.site.register(Add_vaccines)
# admin.site.register(addvaccinedate)
# admin.site.register(vaccine_date)
# admin.site.register(book_add)



# admin.site.register(Account)
def export_reg(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="registration.csv"'
    writer = csv.writer(response)
    writer.writerow(['Username', 'Email', 'phonenumber', 'Address', 'City', 'Pincode','district'])
    registration = queryset.values_list('username', 'email', 'phonenumber', 'address', 'city', 'pincode','district')
    for i in registration:
        writer.writerow(i)
    return response


export_reg.short_description = 'Export to csv'


class RegAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'phonenumber', 'address', 'city', 'pincode','district','is_hospital','is_child','is_ashaworker']
    actions = [export_reg]


admin.site.register(Account,RegAdmin)
class Viewvaccine(admin.ModelAdmin):
    list_display = ['vaccine_name', 'disease', 'no_dose']
    actions = [export_reg]


admin.site.register(Add_vaccines,Viewvaccine)
class Viewstock(admin.ModelAdmin):
    list_display = ['vaccine_name', 'hospital_name','vaccination_date']
    actions = [export_reg]


admin.site.register(new_stock,Viewstock)
# class Viewbook(admin.ModelAdmin):
#     list_display = ['vaccination_date','hospital_name','vaccine_name','child_name']
#     actions = [export_reg]


# admin.site.register(book_add,Viewbook)

# Register your models here.
