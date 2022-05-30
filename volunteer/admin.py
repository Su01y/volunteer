from django.contrib import admin
from volunteer.models import Volunteer
from addresses.models import Task

# Register your models here.

admin.site.register(Volunteer)
admin.site.register(Task)
# @admin.register(Volunteer)
# class VolunteerAdmin(admin.ModelAdmin):
#     pass