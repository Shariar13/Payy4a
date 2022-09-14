from ast import Not
from multiprocessing import context
from typing_extensions import Self
from unicodedata import name
from urllib import request
from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.views import generic
from django.views.generic import ListView, DetailView, TemplateView, UpdateView
from django.contrib.auth.forms import UserChangeForm
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
import re
from .models import userprofile
from .models import job_database
from .models import gig_database
from .models import job_request_database


def home(request):
    return render(request, 'index.html')


class profile(ListView):
    model = userprofile
    template_name = "profile.html"

    def get_context_data(self, *args, **kwargs):
        context = super(profile, self).get_context_data(*args, **kwargs)
        context['job_database'] = job_database.objects.all()
        return context


def gig_post(request):
    return render(request, "gig_post.html")


def hire(request):
    context = {}
    context['userprofile'] = userprofile.objects.all()
    if userprofile.objects.filter(username=request.user):
        return render(request, "employee.html", context)
    else:
        return render(request, 'profile_form.html')


def employee_list(request):
    if request.method == "GET":
        category = request.GET['category']
    if category == "Web Development":
        context = {
            "web_development": gig_database.objects.filter(job_role="Full-Stack Developer"),
            "category": "Web Development"
        }
    elif category == "Graphics Design":
        context = {
            "graphics_design": gig_database.objects.filter(job_role="Graphics Designer"),
            "category": "Graphics Designer"
        }
    elif category == "Python Developer":
        context = {
            "python_developer": gig_database.objects.filter(job_role="Python Developer"),
            "category": "Python Developer"
        }
    elif category == "Rails Developer":
        context = {
            "rails_developer": gig_database.objects.filter(job_role="Rails Developer"),
            "category": "Rails Developer"
        }
    elif category == "PHP Developer":
        context = {
            "php_developer": gig_database.objects.filter(job_role="PHP Developer"),
            "category": "PHP Developer"
        }
    elif category == "Node.js Developer":
        context = {
            "node_developer": gig_database.objects.filter(job_role="Node.js Developer"),
            "category": "Node.js Developer"
        }
    elif category == "Wordpress Developer":
        context = {
            "wordpress_developer": gig_database.objects.filter(job_role="Wordpress Developer"),
            "category": "Wordpress Developer"
        }
    elif category == "Android Developer":
        context = {
            "android_developer": gig_database.objects.filter(job_role="Android Developer"),
            "category": "Android Developer"
        }
    elif category == "iOS Developer":
        context = {
            "ios_developer": gig_database.objects.filter(job_role="iOS Developer"),
            "category": "iOS Developer"
        }
    elif category == "Animation Designer":
        context = {
            "animation": gig_database.objects.filter(job_role="Animation Designer"),
            "category": "Animation Designer"
        }
    elif category == "Cartoon Designer":
        context = {
            "cartoon_designer": gig_database.objects.filter(job_role="Cartoon Designer"),
            "category": "Cartoon Designer"
        }
    elif category == "Logo Designer":
        context = {
            "logo_designer": gig_database.objects.filter(job_role="Logo Designer"),
            "category": "Logo Designer"
        }
    elif category == "Figma Designer":
        context = {
            "figma_designer": gig_database.objects.filter(job_role="Figma Designer"),
            "category": "Figma Designer"
        }
    elif category == "Video Editing":
        context = {
            "video_editing": gig_database.objects.filter(job_role="Video Editing"),
            "category": "Video Editing"
        }
    elif category == "Cyber Security":
        context = {
            "cyber_security": gig_database.objects.filter(job_role="Cyber Security"),
            "category": "Cyber Security"
        }
    elif category == "Content Writing":
        context = {
            "content_writing": gig_database.objects.filter(job_role="Content Writing"),
            "category": "Content Writing"
        }
    elif category == "Research Paper":
        context = {
            "research_paper": gig_database.objects.filter(job_role="Research Paper"),
            "category": "Research Paper"
        }
    elif category == "Artificial Intelligent":
        context = {
            "artificial_intelligent": gig_database.objects.filter(job_role="Artificial Intelligent"),
            "category": "Artificial Intelligent"
        }
    return render(request, "employee_list.html", context)


class employee_profile(DetailView):
    model = gig_database
    template_name = "employee_profile.html"

    def get_context_data(self, *args, **kwargs):
        context = super(employee_profile, self).get_context_data(
            *args, **kwargs)
        context['userprofile'] = userprofile.objects.all()
        return context


def job(request):
    context = {}
    context['userprofile'] = userprofile.objects.all()
    context['job_database'] = job_database.objects.all()
    if userprofile.objects.filter(username=request.user):
        return render(request, "job.html", context)
    else:
        return render(request, "profile_form.html")


class job_request(DetailView):
    model = job_database
    template_name = "job_request.html"

    def get_context_data(self, *args, **kwargs):
        context = super(job_request, self).get_context_data(
            *args, **kwargs)
        context['job_request'] = job_request_database.objects.all()
        return context


def job_request_f(request):
    if request.method == "POST":
        username = request.POST['username']
        name = request.POST['name']
        email = request.POST['email']
        amount = request.POST['amount']
        time = request.POST['time']
        request_id = request.POST['request_id']
        description = request.POST['description']
        job_request_d = job_request_database(
            username=username, name=name, email=email, amount=amount, time=time, request_id=request_id, description=description)
        job_request_d.save()
        messages.success(request, "Your Job Request Successfully Submitted")
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


class job_request_profile(DetailView):
    model = job_request_database
    template_name = "job_request_profile.html"

    def get_context_data(self, *args, **kwargs):
        context = super(job_request_profile, self).get_context_data(
            *args, **kwargs)
        context['userprofile'] = userprofile.objects.all()
        return context


def contact(request):
    return render(request, 'contacts.html')


def profile_form(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        phone = request.POST['phone']
        account_type = request.POST['account_type']
        bio = request.POST['bio']
        job_role = request.POST['job_role']
        interest = request.POST['interest']

        if request.FILES.get('photo', False):
            photo = request.FILES['photo']
            if first_name == "" or last_name == "" or username == "0" or email == "" or phone == "" or account_type == "" or bio == "" or job_role == "" or interest == "":
                messages.error(request, "No Field Shoub Be Empty")
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            else:
                profile_form_database = userprofile(first_name=first_name, last_name=last_name, username=username, email=email,
                                                    phone=phone, account_type=account_type, bio=bio, job_role=job_role, interest=interest, photo=photo)
                profile_form_database.save()
                messages.success(request, "Updated your profile successfully")
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

        else:
            if first_name == "" or last_name == "" or username == "0" or email == "" or phone == "" or account_type == "" or bio == "" or job_role == "" or interest == "":
                messages.error(request, "No Field Shoub Be Empty")
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

            else:
                profile_form_database = userprofile(first_name=first_name, last_name=last_name, username=username, email=email,
                                                    phone=phone, account_type=account_type, bio=bio, job_role=job_role, interest=interest)
                profile_form_database.save()
                messages.success(request, "Updated your profile successfully")
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def gig_form(request):
    if request.method == "POST":
        name = request.POST['name']
        username = request.POST['username']
        email = request.POST['email']
        phone = request.POST['phone']
        bio = request.POST['bio']
        job_role = request.POST['job_role']
        interest = request.POST['interest']
        money = request.POST['money']

        if request.FILES.get('photo', False):
            photo = request.FILES['photo']
            if name == "" or username == "0" or email == "" or phone == "" or bio == "" or job_role == "" or interest == "" or money == "":
                messages.error(request, "No Field Shoub Be Empty")
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            else:
                gig_form_database = gig_database(name=name, username=username, email=email,
                                                 phone=phone, bio=bio, job_role=job_role, interest=interest, money=money, photo=photo)
                gig_form_database.save()
                messages.success(request, "Updated your GIG successfully")
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

        else:
            if name == "" or username == "0" or email == "" or phone == "" or bio == "" or job_role == "" or interest == "" or money == "":
                messages.error(request, "No Field Shoub Be Empty")
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

            else:
                gig_form_database = gig_database(name=name, username=username, email=email,
                                                 phone=phone, bio=bio, job_role=job_role, interest=interest, money=money)
                gig_form_database.save()
                messages.success(request, "Updated your GIG successfully")
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def job_post(request):
    return render(request, "job_post.html")


def job_form(request):
    if request.method == "POST":
        name = request.POST['name']
        username = request.POST['username']
        email = request.POST['email']
        job_category = request.POST['job_category']
        job_amount = request.POST['job_amount']
        job_detail = request.POST['job_detail']

        if request.FILES.get('photo', False):
            photo = request.FILES['photo']
            if job_detail == "" or job_category == "" or job_amount == "":
                messages.error(request, "No Field Shoub Be Empty")
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            else:
                job_database_database = job_database(name=name, username=username, email=email,
                                                     job_category=job_category, job_amount=job_amount, job_detail=job_detail, photo=photo)
                job_database_database.save()
                messages.success(request, "Job posted successfully")
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

        else:
            if job_detail == "" or job_category == "" or job_amount == "":
                messages.error(request, "No Field Shoub Be Empty")
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

            else:
                job_database_database = job_database(name=name, username=username, email=email,
                                                     job_category=job_category, job_amount=job_amount, job_detail=job_detail)
                job_database_database.save()
                messages.success(request, "Job posted successfully")
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def signin(request):
    if request.method == 'POST':
        name = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=name, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Email or Password incorrect')

    return render(request, 'signin.html')


def signup(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        if first_name == "":
            messages.error(request, "You must enter Fisrt Name")
            return render(request, 'signup.html')
        last_name = request.POST['last_name']
        if last_name == "":
            messages.error(request, "You must enter Last Name")
            return render(request, 'signup.html')
        username = request.POST['username']
        if username == "":
            messages.error(request, "You must enter Username")
            return render(request, 'signup.html')
        email = request.POST['email']
        if email == "":
            messages.error(request, "You must enter Email")
            return render(request, 'signup.html')
        password = request.POST['password']
        if password == "":
            messages.error(request, "You must enter Password")
            return render(request, 'signup.html')
        confirm_password = request.POST['confirm_password']
        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username already taken")
            elif User.objects.filter(email=email).exists():
                messages.error(request, "Email already taken")

            else:
                user = User.objects.create_user(
                    first_name=first_name, last_name=last_name, username=username, password=password, email=email)
                user.save()
                login(request, user)
                return redirect('/')

        else:
            messages.error(request, 'Password not matched')

    return render(request, 'signup.html')


def signout(request):
    logout(request)
    return redirect("/")
