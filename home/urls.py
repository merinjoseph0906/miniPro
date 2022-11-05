from django.urls import path
from . import views 
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.index, name='home'),
    #path('childreg/',views.childreg,name='childreg'),
    #path('phcreg/',views.phcreg,name='phcreg'),
    #path('hospitalreg/',views.hospitalreg,name='hospitalreg'),
    #path('ashaworkerreg/',views.ashaworkerreg,name='ashaworkerreg'),
    path('two/',views.base),
    path('ten/',views.userbase),
    path('three/',views.ashaworkerbase),
    #path('three/',views.childregistration),
    path('login/',views.login,name='login'),
    path('logout/',views.logout1,name='logout'),
    path('addprofile/',views.addprofile,name='addprofile'),
    #path('six/',views.hospitalregistration),
    path('seven/',views.about),
    path('userhome/',views.userhome,name='userhome'),
    path('ashahome/',views.ashahome,name='ashahome'),
    path('hospitalhome/',views.hospitalhome,name='hospitalhome'),
    path('phchome/',views.phchome,name='phchome'),
    #path('childregistration/',views.childregistration,name='childregistration'),
    path('newregis/',views.signup,name='newregis'),
    path('duplicate/',views.duplicate,name='duplicate'),
    path('viewvaccine/',views.viewvaccine,name='viewvaccine'),
   
    path('change_password/',views.change_password,name='change_password'),
    path('resetpassword_validate/<uidb64>/<token>/', views.resetpassword_validate, name='resetpassword_validate'),
    path('forgotPassword/', views.forgotPassword, name='forgotPassword'),
    path('resetPassword/', views.resetPassword, name='resetPassword'),
    path('searchbar/', views.searchbar, name='searchbar'),
    path('viewvaccinedate/', views.viewvaccinedate, name='viewvaccinedate'),
   
]
