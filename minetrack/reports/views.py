from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.db.models import Sum
from production.models import ProductionRecord
from dispatch.models import DispatchRecord
from logistics.models import TransportCost
from .models import Report

def generate_report(request):
    """Generates a new report from existing data."""
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    if not start_date or not end_date:
        end_date = timezone.now().date()
        start_date = end_date.replace(day=1)

    # Aggregations from other apps
    total_production = ProductionRecord.objects.filter(
        date__range=[start_date, end_date]
    ).aggregate(Sum('amount'))['amount__sum'] or 0

    total_dispatches = DispatchRecord.objects.filter(
        date__range=[start_date, end_date]
    ).aggregate(Sum('quantity'))['quantity__sum'] or 0

    total_transport_cost = TransportCost.objects.filter(
        date__range=[start_date, end_date]
    ).aggregate(Sum('fuel_cost'))['fuel_cost__sum'] or 0

    total_production_cost = ProductionRecord.objects.filter(
        date__range=[start_date, end_date]
    ).aggregate(Sum('cost'))['cost__sum'] or 0

    total_revenue = DispatchRecord.objects.filter(
        date__range=[start_date, end_date]
    ).aggregate(Sum('revenue'))['revenue__sum'] or 0

    profit_or_loss = total_revenue - (total_transport_cost + total_production_cost)

    # Save to the database
    report = Report.objects.create(
        start_date=start_date,
        end_date=end_date,
        total_production=total_production,
        total_dispatches=total_dispatches,
        total_transport_cost=total_transport_cost,
        total_production_cost=total_production_cost,
        total_revenue=total_revenue,
        profit_loss=profit_or_loss,
    )

    # Redirect to summary page
    return redirect('report_summary', report_id=report.id)


def report_summary(request, report_id):
    report = get_object_or_404(Report, id=report_id)
    return render(request, 'reports/report_summary.html', {'report': report})