from django.db import models
from django.contrib.auth.models import User


class userprofile (models.Model):
    first_name = models.CharField(max_length=99, null=True, blank=True)
    last_name = models.CharField(max_length=99, null=True, blank=True)
    username = models.CharField(max_length=99, null=True, blank=True)
    email = models.CharField(max_length=99, null=True, blank=True)
    phone = models.CharField(max_length=99, null=True, blank=True)
    account_type = models.CharField(max_length=99, null=True, blank=True)
    bio = models.CharField(max_length=300, null=True, blank=True)
    job_role = models.CharField(max_length=300, null=True, blank=True)
    interest = models.CharField(max_length=300, null=True, blank=True)
    photo = models.ImageField(upload_to='photo/', blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        if len(self.username) > 50:
            return self.username[:50]+"..."
        return self.username

    @property
    def get_photo_url(self):
        if self.photo and hasattr(self.photo, 'url'):
            return self.photo.url
        else:
            return None


class job_database (models.Model):
    name = models.CharField(max_length=99, null=True, blank=True)
    username = models.CharField(max_length=99, null=True, blank=True)
    email = models.CharField(max_length=99, null=True, blank=True)
    job_category = models.CharField(max_length=99, null=True, blank=True)
    job_amount = models.IntegerField(null=True, blank=True)
    job_detail = models.CharField(max_length=300, null=True, blank=True)
    photo = models.ImageField(upload_to='photo/', blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        if len(self.username) > 50:
            return self.username[:50]+"..."
        return self.username

    @property
    def get_photo_url(self):
        if self.photo and hasattr(self.photo, 'url'):
            return self.photo.url
        else:
            return None


class gig_database (models.Model):
    name = models.CharField(max_length=99, null=True, blank=True)
    username = models.CharField(max_length=99, null=True, blank=True)
    email = models.CharField(max_length=99, null=True, blank=True)
    phone = models.CharField(max_length=99, null=True, blank=True)
    bio = models.CharField(max_length=300, null=True, blank=True)
    job_role = models.CharField(max_length=300, null=True, blank=True)
    interest = models.CharField(max_length=300, null=True, blank=True)
    money = models.IntegerField(null=True, blank=True)
    photo = models.ImageField(upload_to='photo/', blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        if len(self.username) > 50:
            return self.username[:50]+"..."
        return self.username

    @property
    def get_photo_url(self):
        if self.photo and hasattr(self.photo, 'url'):
            return self.photo.url
        else:
            return None

class job_request_database (models.Model):
    name = models.CharField(max_length=99, null=True, blank=True)
    username = models.CharField(max_length=99, null=True, blank=True)
    email = models.CharField(max_length=99, null=True, blank=True)
    amount = models.IntegerField(null=True, blank=True)
    time = models.IntegerField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    request_id = models.IntegerField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True)



    def __str__(self):
        if len(self.username) > 50:
            return self.username[:50]+"..."
        return self.username
