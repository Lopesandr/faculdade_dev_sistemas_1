from django.contrib import admin
from strava.models import Record
# Register your models here.

classes = (Record)
admin.site.register(classes)