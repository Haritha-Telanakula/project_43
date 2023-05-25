from django.shortcuts import render
from django.http import HttpResponse
from app.forms import *

# Create your views here.

def Sign_up(request):
    ufo=UserForm()
    pfo=ProfileForm()
    d={'ufo':ufo,'pfo':pfo}

    if request.method=='POST':
        ufd=UserForm(request.POST)
        pfd=ProfileForm(request.POST)
        if ufd.is_valid() and pfd.is_valid():
            NSUO=ufd.save(commit=False)
            password=ufd.cleaned_data['password']
            NSUO.set_password(password)
            NSUO.save()

            NSPO=pfd.save(commit=False)
            NSPO.username=NSUO
            NSPO.save()
            return HttpResponse('Regsitration is Susssessfulll')
        else:
            return HttpResponse('Not valid')

    return render(request,'Sign_up.html',d)




