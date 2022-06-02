from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from inventory.warehouse.models import Warehouse


@admin.register(Warehouse)
class CountryAdmin(ImportExportModelAdmin):
    model = Warehouse
