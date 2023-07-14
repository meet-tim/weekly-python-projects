from django.contrib import admin
from .models import ObjectViewed,Visitor,number_of_visits
# Register your models here.
admin.site.register(ObjectViewed)
admin.site.register(Visitor)
admin.site.register(number_of_visits)

