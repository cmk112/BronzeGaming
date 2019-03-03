from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass
@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    pass
@admin.register(Platform)
class PlatformAdmin(admin.ModelAdmin):
    pass
@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    pass
@admin.register(Profile)
class EventAdmin(admin.ModelAdmin):
    pass

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'

class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline, )

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)