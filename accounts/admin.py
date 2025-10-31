from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _
from accounts.models.userModel import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    # Campos que aparecem na listagem principal
    list_display = ('id','username', 'email', 'first_name', 'last_name', 'is_staff', 'peso')
    list_filter = ('is_staff', 'is_superuser', 'is_active')

    # Campos disponíveis para edição no formulário de detalhes
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Informações pessoais'), {'fields': ('first_name', 'last_name', 'email', 'dataNascimento', 'peso')}),
        (_('Permissões'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        (_('Datas importantes'), {'fields': ('last_login', 'date_joined')}),
    )

    # Campos mostrados no formulário de criação de novo usuário
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'is_staff', 'is_active'),
        }),
    )

    search_fields = ('username', 'email', 'first_name', 'last_name')
    ordering = ('username',)
