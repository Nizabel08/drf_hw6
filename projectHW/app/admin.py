from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.utils import timezone
from .models import User

admin.site.site_header = "Nizabel's site"
admin.site.site_title = "User registration"
admin.site.index_title = "User portal"


@admin.action(description='Mark selected users as admin')
def make_admin(modeladmin, request, queryset) :
    queryset.update(is_admin = True)


@admin.action(description='Show only users that were created today')
def date_filtering(modeladmin, request, queryset) :
    today = timezone.now().date()
    return queryset.filter(created_at_date = today)

@admin.action(description='mark selected users as non-admin') 
def mark_as_non_admin(modeladmin, request, queryset) :
    queryset.update(is_admin = False)

@admin.register(User) 
class UserAdmin(admin.ModelAdmin) :
    list_display = ('name', 'last_name', 'age', 'created_at', 'is_admin')
    list_filter = ('age', 'is_admin', 'created_at')
    search_fields = ('name', 'last_name')
    ordering = ('name',)
    list_editable = ('age',)
    actions = [make_admin, mark_as_non_admin, date_filtering]


 