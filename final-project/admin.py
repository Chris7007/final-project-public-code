from django.contrib import admin
from.models import Reports


class ReportsAdmin(admin.ModelAdmin):
    list_display = ("user_id_report", "demo_id_report", "report", "read", "action", "timedate", "user_pk", "demo_pk")
    list_filter = ('user_id_report',)
    

admin.site.register(Reports, ReportsAdmin)

