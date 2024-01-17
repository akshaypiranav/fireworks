from django.db import models
import os
import datetime

def getFileName(request,filename):
    now_time=datetime.datetime.now().strftime("%Y%m%d%H:%M:%S")
    new_filename="%s%s"%(now_time,filename)
    return os.path.join('uploads/',new_filename)
# Create your models here.
class Crackers(models.Model):
    name=models.CharField(max_length=100)
    price=models.DecimalField(max_digits=10, decimal_places=2)
    oldprice=models.DecimalField(max_digits=10, decimal_places=2)
    image=models.ImageField(upload_to=getFileName,null=True,blank=True)
    class Meta:
        db_table='datas'