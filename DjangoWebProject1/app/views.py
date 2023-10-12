
"""
Definition of views.
"""

from datetime import datetime
import email
from django.shortcuts import render
from django.http import HttpRequest
from .models import Pupil
from .forms import ListSearch
from .forms import CreateUser

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )

def list(request):
    """Renders the list page."""
#    assert isinstance(request, HttpRequest)
    pupils=[]
    flag=False
    if request.method=='POST':
        form=ListSearch(request.POST)
        pupils=[]
        if form.is_valid():

            school=form.cleaned_data['school']
            fio=form.cleaned_data['fio']
            cls=form.cleaned_data['cls']

            if school!='':
                pupils= Pupil.objects.filter(school=school)
                flag=True
            if fio!='':
                if flag:
                    pupils=pupils.filter(fio__icontains=fio)
                else:
                    pupils=Pupil.objects.filter(fio__icontains=fio)
                    flag=True
            if cls!='0':
                if flag:
                    pupils=pupils.filter(cls=cls)
                else:
                    pupils=Pupil.objects.filter(cls=cls)
                    flag=True

    else:
        form=ListSearch()

         
    return render(
        request,
        'app/list.html',
        {
            'form': form,
            'pupils': pupils,
            'title':'Список',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )


def portfolio(request):
    """Renders the portfolio page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/portfolio.html',
        {
            'title':'Портфолио',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )

def create_user(request):
    
    """Renders the portfolio page."""
    #assert isinstance(request, HttpRequest)

    if request.method == 'POST':

        form = CreateUser(request.POST)
        if form.is_valid():
            login = form.cleaned_data['login']
            password = form.cleaned_data['password']
            password_corr = form.cleaned_data['password_corr']
            fio = form.cleaned_data['fio']
            log_form = BootstrapAuthenticationForm()
            return render(
                request,
                'app/login.html',
                {
                    'form':log_form,
                    'title':'login',
                    'year':datetime.now().year,
                }
            )


    else:
        form = CreateUser()


    return render(
        request,
        'app/create_user.html',
        {
            'form':form,
            'title':'create user',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )