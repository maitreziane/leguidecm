from django.contrib import admin

from apps.attraction.models import Attraction, Category_attraction, Image_Attraction

# Register your models here.
class AttractionAdmin(admin.ModelAdmin):
    list_display = ["category", "title", "ville"]
    

admin.site.register(Category_attraction)
admin.site.register(Image_Attraction)
admin.site.register(Attraction, AttractionAdmin)
