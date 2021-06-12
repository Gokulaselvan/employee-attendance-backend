from django.contrib import admin


from .models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):

    list_display = ['user', 'experience', 'joining_date']
    list_filter = ['designation', 'department', 'shift']

    search_fields = ('user',)


admin.site.register(UserProfile, UserProfileAdmin)
