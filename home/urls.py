from django.contrib import admin
from django.urls import path
from .import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [

    path('', views.home, name='home'),
    path('profile', views.profile.as_view(), name='profile'),
    path('profile_form', views.profile_form, name='profile_form'),
    path('gig_post', views.gig_post, name='gig_post'),
    path('gig_form', views.gig_form, name='gig_form'),
    path('job_form', views.job_form, name='job_form'),
    path('job_post', views.job_post, name='job_post'),
    path('hire', views.hire, name='hire'),
    path('employee_list', views.employee_list, name='employee_list'),
    path('employee_profile/<int:pk>',
         views.employee_profile.as_view(), name='employee_profile'),
    path('job_request/<int:pk>', views.job_request.as_view(), name='job_request'),
    path('job_request_f', views.job_request_f, name='job_request_f'),
    path('job_request_profile/<int:pk>', views.job_request_profile.as_view(),
         name='job_request_profile'),
    path('job', views.job, name='job'),
    path('contact', views.contact, name='contact'),
    path('signin', views.signin, name="signin"),
    path('signup/', views.signup, name="signup"),
    path('signout/', views.signout, name="signout"),
]
