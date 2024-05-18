from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    # Campos a serem exibidos na listagem de usuários no admin
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active')
    # Campos clicáveis na listagem de usuários no admin
    list_display_links = ('username', 'email')
    # Campos que podem ser editados diretamente na listagem de usuários no admin
    list_editable = ('is_staff', 'is_active')
    # Campos a serem usados na busca
    search_fields = ('username', 'email', 'first_name', 'last_name')
    # Campos de filtro
    list_filter = ('is_staff', 'is_active', 'is_superuser', 'groups')
    
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Informações Pessoais', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissões', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Datas Importantes', {'fields': ('last_login', 'date_joined')}),
    )
    # Campos a serem exibidos no formulário de criação de um novo usuário
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'first_name', 'last_name', 'is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
    )
    ordering = ('username',)
    filter_horizontal = ('groups', 'user_permissions',)

admin.site.register(CustomUser, CustomUserAdmin)
