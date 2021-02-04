from django.contrib import admin

from authentication.models import ProfileModel, UserList

admin.site.register(UserList)
admin.site.register(ProfileModel)