from django.db import models
import datetime
import os

from django.contrib.auth.models import User

# Create your models here.


def getFileName(request,filename):
    now_time=datetime.datetime.now().strftime("%Y%m%d%H:%M:%S")
    new_filename="%s%s"%(now_time,filename)
    return os.path.join('uploads/',new_filename)


class businessdata(models.Model):
    username_post=models.CharField(max_length=30,null=False,blank=False)
    owner_name=models.CharField(max_length=30,null=False,blank=False)
    gender=models.CharField(max_length=30,null=False,blank=False)
    company_name=models.CharField(max_length=50,null=False,blank=False)
    description=models.CharField(max_length=500,null=False,blank=False,default='Share moments. Share life.')
    category=models.CharField(max_length=50,null=False,blank=False,default='retail')
    gstin_number=models.CharField(max_length=15,null=False,blank=True)
    reg_number=models.CharField(max_length=21,null=False,blank=True)
    city=models.CharField(max_length=30,null=False,blank=False)
    street_address=models.CharField(max_length=150,null=False,blank=False)
    town_address=models.CharField(max_length=150,null=False,blank=False)
    pincode=models.CharField(max_length=30,null=False,blank=False)
    contact_number=models.CharField(max_length=10,null=False,blank=False)
    email_id=models.EmailField(max_length=60,null=False,blank=True)
    image=models.ImageField(upload_to=getFileName,null=True,blank=True)
    website_link=models.CharField(max_length=100,null=False,blank=True)
    gmaps_link=models.CharField(max_length=100,null=False,blank=True)
    business_work_type=models.CharField(max_length=30,null=False,blank=False)
    created_at=models.DateTimeField(auto_now_add=True)

    def __int__(self):
        return self.id

class meta:

    db_table= 'businessdata'
    

class jobdatas(models.Model):
     username_post=models.CharField(max_length=30,null=False,blank=False)
     job_position=models.CharField(max_length=35,null=False,blank=False)
     upload_date=models.CharField(max_length=20,null=False,blank=False)
     job_timing=models.CharField(max_length=30,null=False,blank=False)
     company_title=models.CharField(max_length=35,null=False,blank=False)
     job_description=models.TextField(max_length=300,null=False,blank=False,default='Best place to work')
     skill_1=models.CharField(max_length=40,null=False,blank=True)
     skill_2=models.CharField(max_length=40,null=False,blank=True)
     skill_3=models.CharField(max_length=40,null=False,blank=True)
     skill_4=models.CharField(max_length=40,null=False,blank=True)
     skill_5=models.CharField(max_length=40,null=False,blank=True)
     job_city=models.CharField(max_length=30,null=False,blank=False)
     job_Address=models.CharField(max_length=100,null=False,blank=False)
     contact_number=models.CharField(max_length=10,null=False,blank=False)
     email_id=models.EmailField(max_length=60,null=False,blank=True)
     website_link=models.CharField(max_length=100,null=False,blank=True)
     gmaps_link=models.CharField(max_length=100,null=False,blank=True)
     created_at=models.DateTimeField(auto_now_add=True)



     def __int__(self):
        return self.id


class meta:

    db_table= 'jobdatas'
    