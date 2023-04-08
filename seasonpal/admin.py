from django.contrib import admin
from .models import CustomUser, SeasonLocation, Produce, Note, Suggestion,Resource
class CustomUserAdmin(admin.ModelAdmin):
    model = CustomUser
# Register your models here.
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(SeasonLocation)
admin.site.register(Produce)
admin.site.register(Note)
admin.site.register(Suggestion)
admin.site.register(Resource)