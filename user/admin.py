from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from django.contrib.auth.models import Group

from .models import User
from .forms import CustomUserCreationForm, CustomUserChangeForm


class CustomUserAdmin(UserAdmin):

    form = CustomUserChangeForm # Edit view
    add_form = CustomUserCreationForm # Add view

    #fields to be displayed in the list page
    list_display = ('email', 'username', 'employee_id',
                    'is_admin', 'is_active', 'is_staff')
    
    # fields which should be added for filter
    list_filter = ['is_admin', 'is_active', 'is_staff']

    # Mentioning what are the fields with headers
    fieldsets = (
        ("Credentials", {"fields": ('email', 'password')}),
        ("User Info", {'fields': ('username', 'employee_id')}),
        ("Permissions", {'fields': ('is_active',
         'is_admin', 'is_staff', 'is_superuser')})
    )

    # Fields should be visible in the add view page
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            "fields": ('email', 'username', 'employee_id',
                       'password', 'retype_password',
                       'is_admin', 'is_active', 'is_staff', 'is_superuser'),
        }),
    )

    # Fields which are read only, we need this because of extending from abstractbaseuser
    readonly_fields = ['last_login']

    # Fields which are to be searched in the search fields
    search_fields = ['email', 'employee_id']

    # Pre sort based on
    ordering = ('employee_id',)

# Registering the Model to display in the Admin panel
admin.site.register(User, CustomUserAdmin)

# Unregistering the Group model as we don't require
admin.site.unregister(Group)