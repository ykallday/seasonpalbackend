from django.contrib import admin
from .models import CustomUser, SeasonLocation, Produce, Note, Suggestion,Resource
class CustomUserAdmin(admin.ModelAdmin):
    model = CustomUser
# Register your models here.
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(SeasonLocation, Produce, Note, Suggestion, Resource)