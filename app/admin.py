from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin

# Register your models here.

class UserModel(UserAdmin):
    list_display = ['username','user_type']

admin.site.register(CustomUser,UserModel)
admin.site.register(Grade)
admin.site.register(Month)
admin.site.register(Year)
admin.site.register(Mgmt)
admin.site.register(Staff)
admin.site.register(Staff_Notification)
admin.site.register(Staff_leave)
admin.site.register(Mgmt_leave)
admin.site.register(Mgmt_Feedback)
admin.site.register(Staff_Feedback)
admin.site.register(Mgmt_Notification)

admin.site.register(Product)
admin.site.register(Supplier)
admin.site.register(Purchase)










