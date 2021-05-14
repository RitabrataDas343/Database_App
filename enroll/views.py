from django.shortcuts import render, redirect, HttpResponseRedirect
from .forms import StudentRegistration
from .models import User
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def add_show(request):
    if request.method == 'POST':
        river = ''
        ob = StudentRegistration(request.POST)
        if ob.is_valid():
            nm = ob.cleaned_data['name']
            em = ob.cleaned_data['email']
            bd = ob.cleaned_data['birthdate']
            ro = ob.cleaned_data['roll']
            pw = ob.cleaned_data['password']
            st = ob.cleaned_data['state']
            ds = ob.cleaned_data['district']
            reg = User(name=nm, email=em, birthdate=bd, roll=ro, password=pw, state=st, district = ds)
            reg.save()
            ob = StudentRegistration()     
    else: 
        ob = StudentRegistration()
    river = User.objects.all()
    return render (request, 'enroll/addandshow.html', {'form': ob, 'stu': river})

@login_required
def show_data(request):
    if request.method == 'POST':
        river = ''
        ob = StudentRegistration(request.POST)
        if ob.is_valid():
            nm = ob.cleaned_data['name']
            em = ob.cleaned_data['email']
            bd = ob.cleaned_data['birthdate']
            ro = ob.cleaned_data['roll']
            pw = ob.cleaned_data['password']
            st = ob.cleaned_data['state']
            ds = ob.cleaned_data['district']
            reg = User(name=nm, email=em, birthdate=bd, roll=ro, password=pw, state=st, district=ds)
            reg.save()
            ob = StudentRegistration()
    else: 
        ob = StudentRegistration()
    river = User.objects.all()
    return render (request, 'enroll/showdata.html', {'form': ob, 'stu': river})

@login_required
def delete_data(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')

@login_required
def update_data(request, id):
    if request.method == 'POST':
        pi= User.objects.get(pk=id)
        ob = StudentRegistration(request.POST, instance=pi)
        if ob.is_valid():
           ob.save()
        else:
            pi= User.objects.get(pk=id)
            ob = StudentRegistration(instance=pi)
    return render(request, 'enroll/updatestudent.html', {'form':ob})

@login_required
def show_profile(request, id):
    if request.method == "POST":
        pi = User.objects.get(pk=id)                    
        return render(request, 'enroll/showprofile.html', {'pi':pi})




 
       



