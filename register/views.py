from django.shortcuts import render, redirect
from .forms import registerform
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from enroll.models import User
from django.shortcuts import get_object_or_404, render, HttpResponseRedirect
# Create your views here.

def register(rq):
    if rq.method == 'POST':
        form = registerform(rq.POST)
        if form.is_valid():
            form.save()
        return redirect('/login/')
    else:
        form = registerform()
    return render(rq, "register/register.html",{"form":form})

@login_required
def home(request):
    return render(request,'enroll/addandshow.html')
