#from http.client import HTTPResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse
#from . models import tbl_childregistration
#from django.contrib.auth.models import 
#from django.contrib import messages,authp
from django.contrib.auth import login, authenticate
from django.http import HttpResponse
from .models import Account
from .models  import tbl_addprofile,addvaccine,vaccinedate
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage
from django.core.mail import send_mail
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
    Addvaccine = addvaccine.objects.all()

    return render(request,"view vaccination.html",{'vaccine':Addvaccine})
def viewvaccinedate(request):
    date = vaccinedate.objects.all()

    return render(request,"view vaccinedate.html",{'vaccination':date})
# def searchbar(request):
#     if request.method == 'GET':
#         query = request.GET.get('query')
#         if query:
#             Addvaccine = addvaccine.objects.filter(vaccinename_contains=query)
#             return render(request,'searchbar.html',{'Addvaccine': Addvaccine})
#         else:
#             print("no informations to show")
#             return request(request,'searchbar.html',{})
def searchbar(request):
    if request.method == 'GET':
        query = request.GET.get('query')
        if query:
            Addvaccine = addvaccine.objects.filter(vaccinename__icontains=query) 
            return render(request, 'searchbar.html', {'Addvaccine':Addvaccine})
        else:
            print("No information to show")
            return render(request, 'searchbar.html', {})


    















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
  
# def childreg(request):
#     print('0')
#     if request.method=='POST':
#         username=request.POST['username']
#         first_name=request.POST['first_name']
#         last_name=request.POST['last_name']
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
#                 user=User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password)
#                 user.save();
#             print("User Created");
#             return redirect('home')
#         else:
#             messages.info(request,"password not match")
#             return redirect('childreg')
#     else:
        
#           return render(request,'childregis.html')
    
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


