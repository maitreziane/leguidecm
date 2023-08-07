from django.contrib import admin
from apps.hebergement.models import hebergement, Images_Hebergement
# Register your models here.

class HebergementAdmin(admin.ModelAdmin):
    list_display = ["name_heb","localisation"]

class ImageAdmin(admin.ModelAdmin):
    
    list_display =["model", "image"]

admin.site.register(hebergement, HebergementAdmin)
admin.site.register(Images_Hebergement, ImageAdmin)