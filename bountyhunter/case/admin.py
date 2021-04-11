from django.contrib import admin
from .models import Case

# Register your models here.
@admin.register(Case)
class CaseAdmin(admin.ModelAdmin):
    list_display = ['case_name', 'hunter', 'date_from', 'date_to', 'active']
    list_filter = ['date_from', 'date_to', 'active']
    search_fields = ['case_name']