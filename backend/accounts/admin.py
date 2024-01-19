from django.contrib import admin
from accounts.models import User
from import_export.admin import ImportExportModelAdmin


@admin.register(User)
class UserAdmin(ImportExportModelAdmin):
    pass
