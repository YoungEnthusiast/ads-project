from django.contrib import admin
from .models import Person
from .forms import CustomRegisterForm
# from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

class PersonAdmin(UserAdmin):
    list_display = ['created', 'username', 'email', 'type', 'is_staff', 'is_superuser']
    list_display_links = ['username']
    search_fields = ['username']
    list_filter = ['is_staff', 'is_superuser', 'type']
    list_editable = ['is_staff', 'is_superuser']
    list_per_page = 1000

    add_form = CustomRegisterForm
    fieldsets = (
            *UserAdmin.fieldsets,
            (
                "Custom Fields",
                {
                    'fields': ('type',)
                }
            )
        )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'type',)}
        ),
    )
admin.site.register(Person, PersonAdmin)
