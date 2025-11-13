from .models import Book
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.forms import TextInput, Textarea
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('email', 'username', 'date_of_birth', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active')

    fieldsets = (
        (None, {'fields': ('email', 'username', 'password')}),
        ('Personal Info', {'fields': ('date_of_birth', 'profile_photo')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important Dates', {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )

    search_fields = ('email', 'username')
    ordering = ('email',)


# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_filter = ("title", "author", "publication_year",)

    search_fields = ("title", "author",)


admin.site.register(Book, BookAdmin)
admin.site.register(CustomUser, CustomUserAdmin)
