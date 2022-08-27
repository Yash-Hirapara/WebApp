from django.shortcuts import render,redirect
from .models import contact,signup_master
from .forms import contactForm,signup_masterForm,basketForm
from django.contrib import messages
from django.contrib.auth import logout
from .models import basket as bb

# Create your views here.
def login(request):
    if request.method=='POST':
        unm=request.POST['uname']
        pas=request.POST['passwd']

        user=signup_master.objects.filter(uname=unm,passwd=pas)
        #userid=signup_master.objects.get(uname=unm)
        if user:
            print('Login Successfully')
            request.session['user']=unm
            #request.session['userid']=userid.id
            return redirect('/')
        else:
            print('Login Failed.')
    return render(request,'login.html')

def signup(request):
    if request.method=='POST':
        newuser=signup_masterForm(request.POST)
        if newuser.is_valid():
            newuser.save()
            return redirect('/login')
        else:
            print(newuser.errors)
    else:
        newuser=signup_masterForm()
    return render(request, 'signup.html',{'newuser':newuser})

def index(request):
    user=request.session.get('user')
    #userid=request.session.get('userid')
    '''if user==None:
        return render(request,'index.html',{'user':user})
    else:
        pd=signup_master.objects.get(uname=user)
        usid=pd.id
        uid=signup_master.objects.get(id=usid)
        if request.method=='POST':
            upfm=signup_masterForm(request.POST)
            if upfm.is_valid():
                upfm=signup_masterForm(request.POST,instance=uid)
                upfm.save()
                return redirect('profile')
            else:
                print(upfm.errors)     
        return render(request,'index.html',{'user':user,'pd':pd,'manu':manu,'cuser':signup_master.objects.get(id=usid)})'''
    return render(request,'index.html',{'user':user})

def about(request):
    user=request.session.get('user')
    return render(request,'about.html',{'user':user})

def contactus(request):
    user=request.session.get('user')
    if request.method=='POST':
        usfm=contactForm(request.POST)
        if usfm.is_valid():
            usfm.save()
            messages.success(request,'Thanks For Contacting Us.')
            print("Data Saved Successfully")
        else:
            print(usfm.errors)
    return render(request, 'contactus.html',{'user':user})

def userlogout(request):
    logout(request)
    return redirect('/')

def profile(request):
        user=request.session.get('user')
        pd=signup_master.objects.get(uname=user)
        userid=pd.id
        return render(request,'profile.html',{'user':user,'cuser':signup_master.objects.get(id=userid)})

def updateprofile(request):
        user=request.session.get('user')
        pd=signup_master.objects.get(uname=user)
        userid=pd.id
        uid=signup_master.objects.get(id=userid)
        if request.method=='POST':
            upfm=signup_masterForm(request.POST)
            if upfm.is_valid():
                upfm=signup_masterForm(request.POST,instance=uid)
                upfm.save()
                return redirect('profile')
            else:
                print(upfm.errors)
        return render(request,'updateprofile.html',{'user':user,'cuser':signup_master.objects.get(id=userid)})

def basket(request):
    user=request.session.get('user')
    if request.method=='POST':
        bk=basketForm(request.POST)
        if bk.is_valid():
            bk.save()
            return redirect('/#manu')
        else:
            print(bk.errors)
    return render(request,'index.html',{'user':user})

def checkout(request):
    user=request.session.get('user')
    if bb.objects.count()==0:
        empty='Cart Is Empty'
    else:
        ord=bb.objects.all()
        return render(request,'checkout.html',{'user':user,'ord':ord})
    return render(request,'checkout.html',{'user':user,'empty':empty})

def removeitem(request,id):
    user=request.session.get('user')
    usmodel=bb.objects.get(id=id)
    usmodel.delete()
    return redirect('/checkout')

def finalbill(request):
    user=request.session.get('user')
    bb.objects.all().delete()
    return redirect('/')
