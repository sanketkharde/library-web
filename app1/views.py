from multiprocessing import context
from urllib import response
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Books
from .forms import Bookform
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.sessions.models import Session

# Create your views here.
def home(request):
    if request.session.has_key('username'):
        return render(request,'home.html')

    
    return redirect('test')
    

def load_form(request):
    form = Bookform
    return render(request,'index.html',{"form":form})

def add(request):
    if request.session.has_key('username'):
        form = Bookform(request.POST)
        form.save()
        return redirect('show')

    return redirect('test')
   

def show(request):
    if request.session.has_key('username'):
        books= Books.objects.all

        return render(request,'show.html',{'books':books})

    return redirect('test')
    
def edit(request,id):
    books = Books.objects.get(id=id)
    return render(request,'edit.html',{'books':books})

def update(request,id):
    books= Books.objects.get(id=id)
    form = Bookform(request.POST, instance=books)
    form.save()
    return redirect('show')

def delete(request,id):
    books = Books.objects.get(id=id)
    books.delete()
    return redirect('show')
    
def search(request):
    given_name = request.POST['name']
    books = Books.objects.filter(book_name=given_name)
    return render(request,'show.html',{'books':books})

def register(request):
    
    if request.method=="POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username taken")

                return redirect('register')

            elif User.objects.filter(email=email).exists():
                messages.info(request,"username taken")

                return redirect('register')

            else:
                user = User.objects.create_user(first_name=first_name,last_name=last_name,username=username,password=password1,email=email)
                user.save()
                messages.info(request,"user created")
                
                return redirect("test")



            

        else:
            messages.info(request,"please enter valid password.....")
            return redirect('register')

        
            return redirect('test')

    else:

        return render(request,'register.html')

def login(request):
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request, user)
            auth.login(request,user)
            request.session['is_logged']=True
            user = request.user.username
            request.session["username"] = user
            messages.success(request, "successfully logged in")

            response= redirect("home")
            response.set_cookie("username",username)
            response.set_cookie("login_status",True)

            return response
            #return redirect("home")

        else:
            messages.info(request,"invalid credentials")
           
            return redirect("test")


    else:
        
        return render(request,'test.html')


def logout(request):
    response= redirect("test")
    response.delete_cookie("username")
    response.delete_cookie("login_status")

    auth.logout(request)
    return response
    
    #return redirect("test")

def first(request):
    return render(request,'first.html')


def test(request):
    return render(request,'test.html')