from django.db import models


# Create your models here.
from django.db import models
from django.http import HttpResponse
from django.shortcuts import render


class item(models.Model):
    id=models.AutoField
    name=models.CharField(max_length=50)
    price=models.CharField(max_length=50)
    description=models.CharField(max_length=300)
    image=models.ImageField(upload_to="shop/images",default="")

    def __str__(self):
        return self.name






class item2(models.Model):
    id=models.AutoField
    name=models.CharField(max_length=50,default="")
    price=models.CharField(max_length=50,default="")
    description=models.CharField(max_length=500,default="")
    amazonlink=models.CharField(max_length=500,default="")
    flipcart=models.CharField(max_length=500,default="")
    imageurl=models.CharField(max_length=500,default="")
    image=models.ImageField(upload_to="shop/images",default="")
    def __str__(self):
        return self.name


class help(models.Model):
    id=models.AutoField
    name=models.CharField(max_length=50,default="")
    phonenumber=models.CharField(max_length=50,default="")
    email=models.CharField(max_length=50,default="")
    massage=models.CharField(max_length=500,default="")

    def __str__(self):
        return self.phonenumber


class order(models.Model):
    id=models.AutoField
    full_name=models.CharField(max_length=50)
    contect_number=models.CharField(max_length=15)
    email_address=models.CharField(max_length=50)
    address=models.CharField(max_length=150)
    quantity=models.CharField(max_length=50)

    def __str__(self):
        return self.contect_number






def oderupdate(request):
    print("..................now..............")

    name= request.POST.get('username')
    contect=request.POST.get('contectnumber')
    email= request.POST.get('email')
    address= request.POST.get('cusername')
    quantity= request.POST.get('qu')
    print(name,contect,email,address,quantity)
    orderid=request.POST.get('orderid')
    print("this is oredr id "+orderid)


    addpro =order(full_name=name+"_Id:-"+orderid, contect_number=contect, email_address=email,address=address,quantity=quantity)
    addpro.save()

    return render(request,'mainhome.html')



def helpm(request):
    namew = request.POST.get('name')
    contect = request.POST.get('contect')
    email = request.POST.get('email')
    massage = request.POST.get('massage')
    print(namew,contect,email,massage)
    addpro = help(name=namew,phonenumber=contect,email=email,massage=massage)
    addpro.save()
    return render(request, 'mainhome.html')
