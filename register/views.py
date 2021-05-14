from django.shortcuts import render, redirect
from .forms import registerform
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render, HttpResponseRedirect
# Create your views here.

def register(rq):
    if rq.method == 'POST':
        form = registerform(rq.POST)
        if form.is_valid():
            form.save()
            messages.success(rq, 'Registration Successful!!')
            return redirect('/')
        else:
            form = registerform()
            messages.error(rq, 'Invalid Registration')
            return redirect('/')
    else:
        form = registerform()
    return render(rq, "register/register.html",{"form":form})

