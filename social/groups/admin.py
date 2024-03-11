from django.contrib import admin
from . import models
# Register your models here.

# this TabularInline allows us to edit the member model from the admin page
class GroupMemberInline(admin.TabularInline):
    model = models.GroupMember

admin.site.register(models.Group)
