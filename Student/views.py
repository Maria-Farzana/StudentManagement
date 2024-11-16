from django.shortcuts import render,redirect
from.models import *
from.forms import *


# Create your views here.
def home(request):
    maria=management.objects.all()
    context={'maria':maria}
    return render(request,'home.html',context=context)
    
def details(request,id):
    details=management.objects.get(pk=id)
    context={'details':details}
    return render(request,'details.html',context=context)

def upload(request):
    form= FarzanaForm()
    if request.method=='POST':
        form=FarzanaForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    context={'form':form}
    return render(request,'upload.html',context=context)

def update(request,id):
    details=management.objects.get(pk=id)
    form=FarzanaForm(instance=details)
    if request.method=='POST':
        form=FarzanaForm(request.POST,request.FILES,instance=details)
        if form.is_valid():
            form.save()
            return redirect('home')
    context={'form':form}
    return render(request,'upload.html',context=context)

def delete(request,id):
    details=management.objects.get(pk=id)
    if request.method=='POST':
        details.delete()
        return redirect('home')
    return render(request,'delete.html',{'details':details})