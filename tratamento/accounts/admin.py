from django.contrib import admin
from .forms import UserCreationForm, UserChangeForm
from .models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = User

    list_display = ('name', 'CPF')
    search_display = ('name', 'CPF')
    fieldsets = (
        (None, {'fields': ('CPF', 'password')}),
        ('Personal info', {'fields': ('name',)}),
        ('Permissions', {'fields': ('is_active', 'is_superuser', 'is_staff', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('name', 'CPF'),
        }),
    )
    search_fields = ('name', 'CPF')
    ordering = ('name',)


admin.site.site_url = 'Tratamento - Gerência de projetos'
admin.site.index_title = 'Área administrativa'
admin.site.site_header = 'Área administrativa'