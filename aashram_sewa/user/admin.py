from django.contrib import admin

from user.models import user_form
class UserFormAdmin(admin.ModelAdmin):
    list_display=('email', 'phone','date_of_arrival','time_of_help','duration_of_help','age','sleep_dormitory')
    list_filter = ['date_of_arrival','time_of_help','duration_of_help','age','sleep_dormitory']
admin.site.register(user_form, UserFormAdmin)

# Register your models here.
