from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from recommendation.models import Tours


@admin.register(Tours)
class ToursAdmin(ImportExportModelAdmin):
    pass
