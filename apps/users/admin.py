from django.contrib import admin
from apps.users.models import GuideUser, Profil_User
from django.contrib.auth.admin import UserAdmin


class AccountAdmin(UserAdmin):
    
    list_display = ('username','email','date_joined', 'last_login', 'is_admin','is_staff')
    search_fields=('username','email',)
    readonly_fields=('date_joined', 'last_login')
    filter_horizontal= ()
    list_filter =('is_admin','is_staff','is_active')
    fieldsets=()
    

    
admin.site.register(GuideUser, AccountAdmin)
admin.site.register(Profil_User)