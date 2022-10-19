from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout


# Models
from .models import User, Phones, ContactFeedback

# Create your views here.

# 404 Page
class Error(View):
    def get(self, request):
        template = "other/error.html"
        return render(request, template)

# Homepage
class Home(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse('login')) 
        template = "home/index.html"
        phones = Phones.objects.all()
        context = {
            "phones": phones
        }
        return render(request, template, context = context)



# LOGIN / REGISTRATION SYSTEM
class Login(View):
    def get(self, request):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse('homepage'))
        else:
            return render(request, "auth/login.html")

    def post(self, request):
        if request.method == "POST":
            username = request.POST["username"].lower()
            password = request.POST["password"]
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('homepage'))
            else:
                context = {
                    "message": "Invalid username or password!"
                }
                template = "auth/login.html"
                return render(request, template, context)

class Register(View):
    def get(self, request):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse('homepage'))
        else:
            return render(request, "auth/register.html")
    
    def post(self, request):
        if request.method == "POST":
            username = request.POST["username"].lower()
            password = request.POST["password"]
            email = request.POST["email"]
            confirmation = request.POST["confirmation"]

            if password != confirmation:
                return render(request, "auth/register.html", {"message": "Confirm password did not match!"})

            if User.objects.filter(email=email).count() == 1:
                return render(request, "auth/register.html", {"message": "Email address already taken!"})
            try:
                user = User.objects.create_user(username=username, password=password, email=email)
                user.save()
                login(request, user)
                return HttpResponseRedirect(reverse('homepage'))
            except:
                return render(request, "auth/register.html", {"message": "Username already registered!"})

class Logout(View):
    def get(self, request):
        if request.user.is_authenticated:
            logout(request)
            return HttpResponseRedirect(reverse('homepage'))
        else:
            return HttpResponseRedirect(reverse('login'))

class AddPhone(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse('login')) 
        return render(request, "other/addphone.html")

    def post(self,request):
        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse('login'))
        name = request.POST.get("name")
        model = request.POST.get("model")
        processor = request.POST.get("processor")
        price = request.POST.get("price")
        os = request.POST.get("os")
        ram = request.POST.get("ram")
        picture = request.POST.get("fileinput")
        print(picture)
        Phones.objects.create(name=name, model_no=model, processor=processor, price=price, phone_os=os, ram=ram)
        return render(request, "other/addphone.html", {"message": "Phone Added!"})

class ListPhone(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse('login')) 
        template = "other/list.html"
        phones = Phones.objects.all()
        context = {
            "phones": phones
        }
        return render(request, template, context = context)


class AboutUs(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse('login')) 
        
        return render(request, "other/aboutus.html")

class ContactUs(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse('login')) 
        
        return render(request, "other/contactus.html")

    def post(self,request):
        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse('login'))
        firstname = request.POST.get("fullname")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        comments = request.POST.get("comments")
        ContactFeedback.objects.create(full_name=firstname, contact_num=phone, email=email, subject=subject, message=comments)
        return render(request, "other/contactus.html", {"message": "Request Sent!"})

class Privacy(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse('login')) 
        
        return render(request, "other/privacy.html")