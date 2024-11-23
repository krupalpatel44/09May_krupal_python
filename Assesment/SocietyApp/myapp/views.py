from django.shortcuts import render,redirect
from .forms import *
from django.contrib.auth import logout
from django.core.mail import send_mail
import random
from SocietyApp import settings

# Create your views here.

def login(request):
    if request.method=='POST':
        em=request.POST['email']
        pas=request.POST['password']

        user=registerdata.objects.filter(email=em,password=pas)
        if user:
            print("login success...")
            request.session['user']=em
            return redirect('index')
        else:
            print('error... login failed.')
    return render(request,'login.html')

def register(request):
    if request.method=='POST':
        rf=registerform(request.POST,request.FILES)
        if rf.is_valid():
            email=rf.cleaned_data.get('email')
            try:
                registerdata.objects.get(email=email)
                print("email allready exists....")
            except registerdata.DoesNotExist:

                # send email

                global otp
                otp=random.randint(111111,999999)
                fnm=request.POST['firstname']
                sub='Otp Verification'
                msg=f'Dear {fnm} \n\n Thank You For Using Our Services, Your Account Has Been Created...\n\n Your One Time Password Is {otp}.'
                from_id=settings.EMAIL_HOST_USER
                to_id=[request.POST['email']]

                send_mail(subject=sub,message=msg,from_email=from_id,recipient_list=to_id)
                rf.save()
                print('success register')
                return redirect('otpverify')
        else:
            print(rf.errors)
    return render(request,'register.html')

def index(request):
    
    user=request.session.get('user')
    notice=noticedata.objects.all().filter(email=user)
    for i in notice:
        print(i.email)
    return render(request,'index.html',{'user':user,'notice':notice})

def smember(request):
    sreg=registerdata.objects.all()
    return render(request,'smember.html',{'sreg':sreg})

def swatchman(request):
    swatchman=watchman.objects.all()
    return render(request,'swatchman.html',{'swatchman':swatchman})

def notice(request):
    notice=noticedata.objects.all()
    return render(request,'notice.html',{'notice':notice})

def event(request):
    events=eventdata.objects.all()
    return render(request,'event.html',{'events':events})

def profile(request):
    uid=request.session.get('user')
    cid=registerdata.objects.get(email=uid)
    print('id',cid.firstname)
    if request.method=='POST':
        form=registerupdateform(request.POST,instance=cid)
        if form.is_valid():
            form.save()
            print('Data updated...')
            return redirect('index')
        else:
            print(form.errors)
    return render(request,'profile.html',{'user':cid})

def userlogout(request):
    logout(request)
    return redirect('/')

def otpverify(request):
    msg=''
    global otp
    if request.method=="POST":
        if request.POST['otp']==str(otp):
            print("otp verify success.")
            msg='OTP Verification Is Success.........'
            return redirect('/')
        else:
            print("OTP Verification Is Failed......")
            msg='OTP Verification Is Failed.........'
    return render(request,'otpverify.html',{'msg':msg})

def resetpass(request):
    if request.method=='POST':
        newpass=passform(request.POST)
        uid=request.session.get('uid')
        cid=registerdata.objects.get(id=uid)
        if newpass.is_valid():
            newpass=passform(request.POST,instance=cid)
            newpass.save()
            print('Password Reset Successfully')
            return redirect('/')
        else:
            print(newpass.errors)

    return render(request,'resetpass.html')

def emailverify(request):
    if request.method=='POST':
        email=request.POST['email']
        umail=registerdata.objects.get(email=email)
        request.session['uid']=umail.id
        return redirect('resetpass')
    else:
        print('Error...')
    return render(request,'emailverify.html')


