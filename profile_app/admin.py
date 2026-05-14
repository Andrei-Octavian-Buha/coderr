from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from profile_app.models import UserProfile
from rest_framework.authtoken.models import Token

class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = "Users Profile"
    fk_name = 'user'

class UserAdmin(BaseUserAdmin):
    inlines = (UserProfileInline, )
    list_display = ('id','username', 'email', 'first_name', 'last_name', 'is_staff', 'get_type')
    readonly_fields = ('display_token',)

    add_fieldsets = BaseUserAdmin.add_fieldsets + (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name'),
        }),
    )
    
    def get_type(self, instance):
        return instance.profile.type
    get_type.short_description = 'Profile Type'

    def display_token(self, instance):
        try:
            token = Token.objects.get(user=instance)
            return token.key
        except Token.DoesNotExist:
            return "Token is on first login generate."
    
    display_token.short_description = 'Auth Token'

    fieldsets = BaseUserAdmin.fieldsets + (
        ('User Token', {'fields': ('display_token',)}),
    )


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
