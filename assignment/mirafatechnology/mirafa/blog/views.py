from django.shortcuts import render
from django.contrib.auth import authenticate,login
from django.shortcuts import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User

from django.views.generic import ListView, View, DetailView
from blog.forms import AuthForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

# def user_login(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(username = username , password = password)
#         if user:
#             if user.is_active:
#                 login(request , user)
#                 return HttpResponseRedirect('/blog/login/')
#             else:
#                 return HttpResponseRedirect('You dont have an account with us')
#         else:
#             print "Invalid Login Details: {0} , {1}".format(username , password)
#             return HttpResponse('Invalid Login Details ')

#     else:
#         return render(request ,'registration/login.html' , {})


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if User.objects.filter(username=username).exists():
            return HttpResponseRedirect('user is already exists')
        else:
            user = User.objects.create_user(username=username, password=password)
            return HttpResponseRedirect('/blog/register/')
    else:
        return render(request ,'registration/register.html' , {})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                request.session.set_expiry(8640) #sets the exp. value of the session
                print request.session.session_key 
                login(request, user) #the user is now logged in
                return HttpResponseRedirect('/blog/about/')
            else:
                return HttpResponseRedirect('You dont have an account with us')
        else:
            print "Invalid Login Details: {0} , {1}".format(username , password)
            return HttpResponse('Invalid Login Details ')
    else:
        return render(request ,'registration/login.html' , {})



from django.views.generic import TemplateView

class AboutView(TemplateView):
    template_name = "abc.html"