from django import forms
from .models import Account,update_profile
class userupdateform(forms.ModelForm):
    # email= forms.EmailField()

    class Meta:
        model = Account
        fields = ['username','phonenumber','address','city','pincode','district']
    


class profileUpdateForm(forms.ModelForm):
     class Meta:
        model = update_profile
        fields = ['name','dob','panchayath']