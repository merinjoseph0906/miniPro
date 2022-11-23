#from http.client import HTTPResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse
#from . models import tbl_childregistration
#from django.contrib.auth.models import 
#from django.contrib import messages,authp
from django.contrib.auth import login, authenticate
from django.http import HttpResponse
from .models import Account, update_profile
from .models  import tbl_addprofile,Add_vaccines,new_stock,about_vaccine,add_timeslot,book_add
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage
from django.core.mail import send_mail
from django.template import loader

from .forms import userupdateform,profileUpdateForm
import datetime
# Create your views here.

def index(request):
    return render(request,"index.html")

def base(request):
    return render(request,'base.html') 
def duplicate(request):
    return render(request,'duplicate.html') 
 

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        print(email,password)
        user=authenticate(email=email,password=password)
        print(user)
        if user is not None:
            #login(user)
            auth.login(request, user)
            # save email in session
            request.session['email'] = email
            if user.is_admin:
                return redirect('http://127.0.0.1:8000/admin/')
            if user.is_child:
                return redirect('userhome')
            if user.is_ashaworker:
                return redirect('ashahome')
            elif user.is_hospital:
                return redirect('hospitalhome')
            elif user.is_PHC:
                return redirect('phchome')    
            else:
                return redirect('/')
        else:
            messages.error(request, 'Invalid Credentials')
            return redirect('login')
    return render(request, 'login.html') 

from django.views.decorators.cache import cache_control
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def logout1(request):
    auth.logout(request)
    return redirect('login')  

def signup(request):
    if request.method == 'POST':
        role=request.POST['role']
        email=request.POST['email']
        username = email.split('@')[0]
        phonenumber=request.POST['phonenumber']
        address=request.POST['address']
        city=request.POST['city']
        pincode=request.POST['pincode']
        district=request.POST['district']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        print('one')
        is_child= is_ashaworker = is_hospital = is_PHC =False
        if role=='is_child':
            is_child=True
        elif role=='is_ashaworker':
            is_ashaworker=True
        elif role=='is_hospital':
            is_hospital=True
        else:
            is_PHC=True
         
        if password==cpassword:
            # if Account.objects.filter(username=username).exists():
            #     messages.info(request,'username taken')
            #     print('3')
            #     return redirect('register/')
            # elif Account.objects.filter(email=email).exists():
            if Account.objects.filter(email=email).exists():

                messages.info(request,'email already taken')
                return redirect('signup')
            else:
                user=Account.objects.create_user(username=username,phonenumber=phonenumber,email=email,address=address,city=city,pincode=pincode,district=district,password=password,is_child=is_child,is_ashaworker=is_ashaworker,is_hospital=is_hospital,is_PHC=is_PHC)
                user.save()
                messages.success(request, 'Thank you for registering with us. Please Login')
                return redirect('login')
        else:
              print("password is not matching")
    else:   
              # return redirect('index.html')
     return render(request,'newregis.html')

def change_password(request):
    if request.method == 'POST':
        current_password = request.POST['current_password']
        new_password = request.POST['new_password']
        confirm_password = request.POST['confirm_password']

        user = Account.objects.get(email__exact=request.user.email)
        success = user.check_password(current_password)
        if success:
            user.set_password(new_password)
            user.save()
            messages.success(request, 'Password updated successfully.')
            return redirect('login')
        else:
            messages.error(request, 'Password does not match!')
            return redirect('change_password/')
    return render(request, 'change_password.html')

def forgotPassword(request):
    if request.method == 'POST':
        email = request.POST['email']
        if Account.objects.filter(email=email).exists():
            user = Account.objects.get(email__exact=email)

            # Reset password email


            current_site = get_current_site(request)
            message = render_to_string('ResetPassword_email.html', {
                'user': user,
                'domain': current_site,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user),
            })

            send_mail(
                'Please activate your account',
                message,
                'evaccination01@gmail.com',
                [email],
                fail_silently=False,
            )
            
            messages.success(request, 'Password reset email has been sent to your email address.')
            return redirect('login')
        else:
            messages.error(request, 'Account does not exist!')
            return redirect('forgotPassword')
    return render(request, 'Forgot_Password.html')

def resetpassword_validate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = Account._default_manager.get(pk=uid)
    except(TypeError, ValueError, OverflowError, Account.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        request.session['uid'] = uid
        messages.success(request, 'Please reset your password')
        return redirect('resetPassword')
    else:
        messages.error(request, 'This link has been expired!')
        return redirect('login')

def resetPassword(request):
    if request.method == 'POST':
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        if password == cpassword:
            uid = request.session.get('uid')
            user = Account.objects.get(pk=uid)
            user.set_password(password)
            user.save()
            messages.success(request, 'Password reset successful')
            return redirect('login')
        else:
            messages.error(request, 'Password do not match!')
            return redirect('resetPassword')
    else:
        return render(request, 'ResetPassword.html')

@login_required(login_url='login')
def userhome(request):
    return render(request,'userhome.html') 
@login_required(login_url='login')
def ashahome(request):
    return render(request,'ashahome.html') 
@login_required(login_url='login')
def hospitalhome(request):
    return render(request,'hospitalhome.html') 
@login_required(login_url='login')
def phchome(request):
    return render(request,'phchome.html') 
def ashaworkerbase(request):
    return render(request,'ashaworkerbase.html') 

@login_required(login_url='login')
def addprofile(request):
    return render(request,'addprofile.html') 
# def signup(request):
#     return render(request,'registration.html') 
def hospitalregistration(request):
    return render(request,'hospitalregistration.html') 
def userbase(request):
    return render(request,'userbase.html') 
def about(request):
    return render(request,'about.html')
def viewvaccine(request):
    Addvaccine = Add_vaccines.objects.all()
    return render(request,"view vaccination.html",{'vaccine':Addvaccine})
def stockdetails(request):

    Stock = new_stock.objects.all()

    return render(request,"view stockss.html",{'stocks':Stock})
def viewvaccinedate(request):
    date = vaccines_date.objects.all()

    return render(request,"view vaccinedate.html",{'vaccination':date})
# def viewstockdetails(request):
#     stocks = addstocks_details.objects.all()

#     return render(request,"viewstockdetails.html",{'stocks':stocks})
# def addstock(request):
  
#     Addstock = add_vaccines.objects.all()
    
    
#     return render(request,'addstock.html',{'vaccination':Addstock})
def viewstock(request):
    Addstock = Add_vaccines.objects.all()
  
    if request.method == 'POST':
        
        available_stock = request.POST.get('available_stock')
        # time_slot = request.POST.get('time_slot')
        hospital_name = request.POST.get('hospital_name')
        vaccine_name = request.POST.get('vaccine_name')
        vaccination_date=request.POST.get('vaccination_date')
        vaccination_type=request.POST.get('vaccination_type')
        addstock=new_stock(vaccine_name_id=vaccine_name,available_stock=available_stock,vaccination_date=vaccination_date,vaccination_type=vaccination_type,hospital_name=hospital_name)
        addstock.save()
        
  
        return redirect('addtimeslot')
    return render(request,'addstock.html',{'vaccination':Addstock}) 
def addtimeslot(request):
    Addstock = Add_vaccines.objects.all()
    stock=new_stock.objects.all()

    if request.method == 'POST':
        
        # available_stock = request.POST.get('available_stock')
        vaccine_name = request.POST.get('vaccine_name')
        hospital_name = request.POST.get('hospital_name')
       
        vaccination_date=request.POST.get('vaccination_date')
        time_slot = request.POST.get('time_slot')
        # vaccination_type=request.POST.get('vaccination_type')
        print(vaccination_date)
        # vaccination_date = vaccination_date.strftime("%Y-%m-%d")
        
        add=add_timeslot.objects.create(vaccine_name_id=vaccine_name,vaccination_date_id=vaccination_date,hospital_name=hospital_name, time_slot = time_slot )
        add.save()
       
  
        # return redirect('')
    return render(request,'add timeslot.html',{'vaccination':Addstock,'Stocks':stock})      
# def searchbar(request):
#     if request.method == 'GET':
#         query = request.GET.get('query')
#         if query:
#             Addvaccine = Add_vaccines.objects.filter(vaccinename_contains=query)
#             return render(request,'searchbar.html',{'Addvaccine': Addvaccine})
#         else:
#             print("no informations to show")
#             return request(request,'searchbar.html',{})
def searchbar(request):
    if request.method == 'GET':
        query = request.GET.get('query')
        if query:
            vaccine_obj=Add_vaccines.objects.filter(vaccine_name=query)
            if vaccine_obj:
                print(vaccine_obj)

                Addvaccine = new_stock.objects.filter(vaccine_name_id=vaccine_obj.id) 
                
                return render(request, 'searchbar.html', {'Addvaccine':Addvaccine})
            else:
                print("No information to show")
                template=loader.get_template('viewslotsearch.html')
                context={
                    'msg': 1,
                    
                }
                return HttpResponse(template.render(context,request))

        else:
            print("No information to show")
            return render(request, 'searchbar.html', {})
def searchslot(request):
    if request.method == 'GET':
        query = request.GET.get('query')
        if query:
            result=[]
            # stock_list=[]
            Addvaccine = Account.objects.filter(district__icontains=query,is_hospital="True")
            is_hospital= Account.objects.filter(district__icontains=query,is_hospital="True")
            is_PHC=Account.objects.filter(district__icontains=query,is_PHC="True")
            stock=new_stock.objects.all()
            # for i in stock:
            #     stock_list.append(i)
            for i in is_hospital:
                result.append(i)
            print(result)
            

            for i in is_PHC:
                result.append(i)
            print(result)
            print(Addvaccine)
            if result:
            # Addvaccine = Account.objects.filter(district__icontains=query,is_PHC="True") 
                return render(request, 'viewslotsearch.html', {'vaccine':result,"stock":stock})
            else:
                print("No information to show")
                template=loader.get_template('viewslotsearch.html')
                context={
                    'msg': 1,
                    
                }
                return HttpResponse(template.render(context,request))
                
        else:

            print("No information to show")
            template=loader.get_template('viewslotsearch.html')
            context={
                'msg': 1,
                
            }
            return HttpResponse(template.render(context,request))
            # return render(request, 'viewslotsearch.html',context)
def profile(request):
    
    if request.user.is_authenticated:
        print(request.user.id)
        # p=update_profile.objects.filter(email__id=request.user.id)
        p=Account.objects.filter(id=request.user.id)
        print(p)
        return render(request,'profile.html', context={'p': p})
    else:
        return render(request,'login.html')
def profile_update(request):
    
    if request.method =='POST':
        u_form  = userupdateform(request.POST)
        p_form = profileUpdateForm(request.POST)
        print("1")
        print(u_form.is_valid())
        print(p_form.is_valid())
        if p_form.is_valid() and u_form.is_valid():
            print("2")
            # p_form.email=1
            # u_form.save()
            p_form.save()
            print('3')
            return redirect('profile')
    
    else:
       u_form  = userupdateform(instance=request.user)
       p_form = profileUpdateForm(instance=request.user)
    
    context={
        'u_form' : u_form,
        'p_form' : p_form,

    }
    return render(request,'profileupdate.html',context)
   
###############################################
def slotsearch(request):
    return render(request,'slotsearch.html')
def aboutvaccine(request):
    if request.method == 'POST':
        
        disease = request.POST.get('disease')
        vaccine = request.POST.get('vaccine')
        disease_spread = request.POST.get('disease_spread')
        symptoms = request.POST.get('symptoms')
        complications=request.POST.get('complications')
       
        about=about_vaccine(disease=disease, vaccine= vaccine,disease_spread=disease_spread,symptoms =symptoms,complications=complications)
        about.save()
    return render(request,'about vaccine.html')
def viewaboutvaccine(request):
    abouts = about_vaccine.objects.all()

    return render(request,"view aboutvaccine.html",{'vaccination':abouts})
def addbooking(request):
    vaccine = Add_vaccines.objects.all()
    stok = new_stock.objects.all()
    slot = add_timeslot.objects.all()
    if request.method == 'POST':
        hospital_name = request.POST.get('hospital_name')
        vaccine_name = request.POST.get('vaccine_name')
        child_name = request.POST.get('child_name')
        dose = request.POST.get('dose')
        vaccination_date=request.POST.get('vaccination_date')
        time_slot = request.POST.get('time_slot')
        
        b=book_add.objects.create(hospital_name=hospital_name,vaccine_name_id=vaccine_name,child_name=child_name,dose=dose,vaccination_date_id=vaccination_date,time_slot_id=time_slot)
        b.save()
        print(hospital_name)
        print(vaccine_name)
        slott=new_stock.objects.get(id=hospital_name)
        
        # print(slot)
    
        # a_stock=slot.available_stock-1
        slott.available_stock+=-1
        slott.save()
    return render(request,"booking.html",{'Stock':stok,'Slot':slot,'vaccine':vaccine})
def viewbooking(request):
    book=book_add.objects.all()
    return render(request,"booking view.html",{'book':book})
#         obj1=Account.objects.get(email))
#         obj=book_add.objects.filter(hospital_name=username)
#         print(obj)
#         print(request.user.id)
#         print(request.user.username)
#         context={'result' : obj }
#         return render(request,'booking view.html',context)
#     else:
#         return render(request,'booking view.html')
    # print(request.session['email'])
    
    
    # user=Account.objects.get(email=request.session['email'],is_hospital=True)
    # print(user)
    # user=request.user
    # print(user)

  
    # hospital_name_obj=new_stock.objects.filter(hospital_name=user.username)
    # book=book_add.objects.all()
    # print(book)
    
    # if request.user.is_authenticated:

    #     obj=book_add.objects.(user=request.user)
    #     print(request.user)
    #     context={'result' : obj }
    #     return render(request,'booking view.html',context)
    # else:
    #     return render(request,'booking view.html')
    # return render(request,"booking view.html",{'book':book})

def continuesearch(request,username):
    user_name=username
    detail_list=new_stock.objects.filter(hospital_name=username)
    print(user_name)
    return render(request,"vsearch continue.html",{'detail':detail_list})


    















def addprofile(request):
    if request.method == 'POST':
        fathersname = request.POST['fathersname']
        mothersname = request.POST['mothersname']
        panchayath = request.POST['panchayath']
        location = request.POST['location']
        weight = request.POST['weight']
        dob = request.POST['dob']
        tbl_addprofile.objects.create(fathersname=fathersname, mothersname=mothersname, panchayath=panchayath, location=location,weight=weight,dob=dob)
        return redirect('userhome')

    return render(request, 'addprofile.html')
  

# def phcreg(request):
#     print('0')
#     if request.method=='POST':
#         username=request.POST['username']
#         email=request.POST['email']      
#         password=request.POST['password']
#         cpassword=request.POST['cpassword']
#         print('one')
#         if password==cpassword:   
#             if User.objects.filter(username=username).exists():
#                 messages.info(request,"email Already Exists")
#                 return redirect('childreg') 
#             elif User.objects.filter(email=email).exists():
#                 messages.info(request,"Email Already Exists")
#                 return redirect('childreg')
            
#             else:
#                 print('two')
#                 user=User.objects.create_user(username=username,email=email,password=password)
#                 user.save();
#             print("User Created");
#             return redirect('home')
#         else:
#             messages.info(request,"password not match")
#             return redirect('phcreg')
#     else:
        
#           return render(request,'phcreg.html')
# def hospitalreg(request):
#     print('0')
#     if request.method=='POST':
#         username=request.POST['username']

#         email=request.POST['email']      
#         password=request.POST['password']
#         cpassword=request.POST['cpassword']
#         print('one')
#         if password==cpassword:   
#             if User.objects.filter(username=username).exists():
#                 messages.info(request,"email Already Exists")
#                 return redirect('hospitalreg') 
#             elif User.objects.filter(email=email).exists():
#                 messages.info(request,"Email Already Exists")
#                 return redirect('hospitalreg')
            
#             else:
#                 print('two')
#                 user=User.objects.create_user(username=username,email=email,password=password)
#                 user.save();
#             print("User Created");
#             return redirect('home')
#         else:
#             messages.info(request,"password not match")
#             return redirect('')
#     else:
        
#           return render(request,'hospitalreg.html') 
# def ashaworkerreg(request):
#     print('0')
#     if request.method=='POST':
#         username=request.POST['username']
#         email=request.POST['email']      
#         password=request.POST['password']
#         cpassword=request.POST['cpassword']
#         print('one')
#         if password==cpassword:   
#             if User.objects.filter(username=username).exists():
#                 messages.info(request,"email Already Exists")
#                 return redirect('ashaworkerreg') 
#             elif User.objects.filter(email=email).exists():
#                 messages.info(request,"Email Already Exists")
#                 return redirect('ashaworkerreg')
            
#             else:
#                 print('two')
#                 user=User.objects.create_user(username=username,email=email,password=password)
#                 user.save();
#             print("User Created");
#             return redirect('home')
#         else:
#             messages.info(request,"password not match")
#             return redirect('')
#     else:
        
#           return render(request,'ashaworkerreg.html')  

#def childregistration(request):
    #return render(request,'registration.html') 
# def login(request):
#     request.session.flush()
#     if 'username' in request.session:
#         return redirect('home')
    
#     if request.method== "POST":
#         username=request.POST['username']
#         password=request.POST['password']
#         user=auth.authenticate(username=username,password=password)
#         if user is not None:
#             auth.login(request, user)
#             return redirect('userhome')
#         else:
#             messages.info(request, 'username or password is incorrect')
#             return redirect('login')
#     else:
         
#       return render(request,'login.html') 


