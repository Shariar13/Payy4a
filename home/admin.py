from django.contrib import admin
from .models import userprofile
from .models import job_database
from .models import gig_database
from .models import job_request_database

admin.site.register (userprofile)
admin.site.register (job_database)
admin.site.register (gig_database)
admin.site.register (job_request_database)
