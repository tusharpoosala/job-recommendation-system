from django.contrib import admin

# Register your models here.

from dailyapp.models import Contact
from dailyapp.models import Employer
from dailyapp.models import Candidate
from dailyapp.models import Add_notification
from dailyapp.models import Preferences



admin.site.register(Contact)
admin.site.register(Employer)
admin.site.register(Candidate)
admin.site.register(Add_notification)
admin.site.register(Preferences)