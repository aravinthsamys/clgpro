from django.shortcuts import redirect, render
from django.core.mail import send_mail
from django.contrib import messages
from ican.form import CustomUserForm
from . models import *
from .form import *
from django.contrib.auth.models import User
from django.conf import settings
from django.shortcuts import redirect
from django.template import loader
from django.http import HttpResponse
from django.db.models import Q
# for login
from django.contrib.auth import authenticate,login,logout


# Create your views here.
def index(request):
   if request.method == 'POST':
    name= request.POST.get("name", "")
    message = request.POST.get("message", "")
    from_email = request.POST.get("from_email")
    msg=message+"     \n    " + from_email

    send_mail(
    name,
    msg,
    from_email,
    ["teramediainfo@gmail.com"],
    fail_silently=False,
              )
    msg1='thankyou, Your message can be catch by a teramedia officials soon '
    namedto='TeraMedia'
    send_mail(
    namedto,
    msg1,
    "teramediainfo@gmail.com",
    [from_email],
    fail_silently=False,
              )
    return redirect('index')
   
#    messages.success(request,'successfully email sent..')
   return render(request,'indexauth/index.html')


def login_page(request):
    # if request.user.is_authenticated:
    #     return redirect("index")
    # else:
        if request.method=='POST':
            name=request.POST.get('username')
            pwd=request.POST.get('password')
            user=authenticate(request,username=name,password=pwd)
            if user is not None:
                login(request,user)
                messages.success(request,'logged in successfully')
                return redirect('profile')
            else:
                messages.error(request,'Incorrect Login Credentials')
                return redirect('/login_page')
        return render(request,'indexauth/login.html')
    

def service(request):
    return render(request,'indexauth/service.html')


# -------
def jobprofile(request):
    userpost=jobdatas.objects.filter(username_post=request.user).order_by("-id")
    return render(request,'indexauth/jobprofile.html',{'userpost':userpost})

def alljobs(request): 
       if request.method=='POST':
         searchedcity1=request.POST.get('searched')
         categoryby=request.POST.get('category')
       
         searched=jobdatas.objects.filter(job_position=categoryby,job_city__icontains=searchedcity1 ).order_by("-id")

             
         return render(request,'indexauth/alljobs.html',{'userpost':searched})
       else:
         userpost=jobdatas.objects.all().order_by("-id") 
         return render(request,'indexauth/alljobs.html',{'userpost':userpost})
       
def jobsubmission(request): 
      if request.method == 'POST':
        
        
        form = ImageFormtwo(request.POST)
        if form.is_valid():
            from_email=request.POST.get('email_id')
            msg1='Dear Customer.,\n\nYour Business details are filled and displayed soon.\ncheck on the page if any changes you want kindly,reply to the teramedia contact site.\n\nThank You\nby TeraMediainfo Officials.. '
            namedto='TeraMedia'
            send_mail(
            namedto,
            msg1,
            "teramediainfo@gmail.com",
            [from_email],
            fail_silently=False,
              )
            form.save()
            return redirect('jobprofile')
      else:
         form = ImageFormtwo()
         print(form.errors)
      return render(request,'indexauth/jobsubmission.html',{'form': form})
# ------




def profile(request): 
      userpost=businessdata.objects.filter(username_post=request.user).order_by("-id")
      return render(request,'indexauth/profile.html',{'userpost':userpost})

def alldatas(request): 
       if request.method=='POST':
         searchedcity1=request.POST.get('searched')
         categoryby=request.POST.get('category')
        #  categoryby1=(categoryby.lower()).strip()
        #  searchedcity1=(searchedcity.lower()).strip()
        #  searched=businessdata.objects.filter(
        #      Q(pincode__icontains=searchedcity1) | 
        #      Q(street_address__icontains=searchedcity1) |
        #      Q(town_address__icontains=searchedcity1) |
        #      Q(city__icontains=searchedcity1) |
        #      Q(owner_name__icontains=searchedcity1) |
        #      Q(username_post__icontains=searchedcity1) |
        #      Q(category__icontains=searchedcity1) |
        #      Q(company_name__icontains=searchedcity1) |
        #      Q(contact_number__icontains=searchedcity1) |
        #      Q(category=categoryby) & Q(category=categoryby,pincode__icontains=searchedcity1)
        #      ) 
         searched=businessdata.objects.filter(category=categoryby,pincode__icontains=searchedcity1 ).order_by("-id")

             
         return render(request,'indexauth/alldatas.html',{'Businessdata':searched})
       else:
         Businessdata=businessdata.objects.all().order_by("-id") 
         return render(request,'indexauth/alldatas.html',{'Businessdata':Businessdata})

def createpost(request): 
      if request.method == 'POST':
        from_email=request.POST.get('email_id')
        msg1='Dear Customer.,\n\nYour Business details are filled and dispalyed soon.\ncheck on the page if any changes you want kindly,reply to the teramedia contact site.\n\nThank You\nby TeraMediainfo Officials.. '
        namedto='TeraMedia'
        send_mail(
        namedto,
        msg1,
        "teramediainfo@gmail.com",
        [from_email],
        fail_silently=False,
              )
        
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('profile')
      else:
         form = ImageForm()
        
      return render(request,'indexauth/createpost.html',{'form': form})

def register(request):
    form=CustomUserForm()
    if request.method=='POST':
        form=CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            from_email=request.POST.get('email')
            msg1='Dear Customer.,\n\nYour Business Account created successfully\n if any queries kindly,reply to the teramedia contact site.\n\nThank You\nby TeraMediainfo Officials.. '
            namedto='TeraMedia'
            send_mail(
            namedto,
            msg1,
            "teramediainfo@gmail.com",
            [from_email],
            fail_silently=False,
              )
            messages.success(request,"Regitration Success")
            return redirect('login_page')
        
    return render(request,'indexauth/register.html',{'form':form})

def logout_page(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request,"logged out successfully")
    return redirect("index")


def fulldetails(request,id):
    data2=businessdata.objects.get(id=id)
    busidata={'data2':data2}
    template=loader.get_template('indexauth/fulldetails.html')
    return HttpResponse(template.render(busidata,request))

def delete_details(request,id):
    data2=businessdata.objects.get(id=id)
    data2.delete()
    return redirect('profile')

def delete_jobdetails(request,id):
    data2=jobdatas.objects.get(id=id)
    data2.delete()
    return redirect('jobprofile')

def edit_fulldetails(request,id):
    data2=businessdata.objects.get(id=id)
    if request.method == 'POST':
        from_email=request.POST.get('email_id')
        msg1='Dear Customer,\n\nYour Business details are Updated soon.\n\nThank You\nby TeraMediainfo Officials. '
        namedto='TeraMedia'
        send_mail(
        namedto,
        msg1,
        "teramediainfo@gmail.com",
        [from_email],
        fail_silently=False,
              )
        
        form = ImageForm(request.POST or None, request.FILES,instance=data2)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
         form = ImageForm()
    busidata={'data2':data2,'form':form}
    template=loader.get_template('indexauth/edit_fulldetails.html')
    return HttpResponse(template.render(busidata,request))


def fulluserdata(request,id):
  if request.method == 'POST':
    sub='Reports'
    reportid1=request.POST.get("report_id")
    reportuser1=request.POST.get("reportuser")
    reportby1=request.POST.get("report_by")
    issue=request.POST.get("issue")
    reportid=str(reportid1)
    reportuser=str(reportuser1)
    reportby=str(reportby1)
    msg='The Reported ID is ' + reportid + ' - ' + reportuser + '\n\nissue : ' + issue + ' \n      by  ' + reportby
    from_email='teramediainfo@gmail.com'

    send_mail(
    sub,
    msg,
    from_email,
    ["teramediainfo@gmail.com"],
    fail_silently=False,
              )
    
  data2=businessdata.objects.get(id=id)
  busidata={'data2':data2}
  return render(request,'indexauth/fulluserdata.html',busidata)

