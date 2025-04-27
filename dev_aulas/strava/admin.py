from django.contrib import admin
from strava.models import Record, Pefil, Clube, LinkSociaisClube
# Register your models here.

classes = (Record, Pefil, Clube, LinkSociaisClube)
admin.site.register(classes)