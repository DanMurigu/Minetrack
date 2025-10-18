from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse
from .models import Report


@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'start_date',
        'end_date',
        'total_sales',
        'total_expenses',
        'profit_loss',
        'view_summary_link',
    )
    readonly_fields = (
        'total_production_cost',
        'total_dispatch_cost',
        'total_logistics_cost',
        'total_sales',
        'total_expenses',
        'profit_loss',
        'created_at',
    )

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        # Make sure your Report model has a method called generate_report()
        if hasattr(obj, 'generate_report'):
            obj.generate_report()

    def view_summary_link(self, obj):
        try:
            url = reverse('reports:report_summary', args=[obj.id])
            return format_html('<a class="button" href="{}">View Breakdown</a>', url)
        except Exception:
            return "No link"
    view_summary_link.short_description = "Breakdown"
