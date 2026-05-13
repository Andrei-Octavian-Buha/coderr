from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from profile_app.models import UserProfile

# Register your models here.

class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = "Users Profile"
    fk_name = 'user'

class UserAdmin(BaseUserAdmin):
    inlines = (UserProfileInline, )
    list_display = ('id','username', 'email', 'first_name', 'last_name', 'is_staff', 'get_type')
    def get_type(self, instance):
        return instance.profile.type
    get_type.short_description = 'Profile Type'


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
