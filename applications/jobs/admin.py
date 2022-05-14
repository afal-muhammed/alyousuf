from django.contrib import admin
from .models import JobOpportunities
from import_export.admin import ImportExportModelAdmin

# Register your models here.
# admin.site.register(JobOpportunities)
@admin.register(JobOpportunities)
class PersonAdmin(ImportExportModelAdmin):
    pass