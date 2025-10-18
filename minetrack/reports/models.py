from django.db import models
from django.utils import timezone
from production.models import ProductionRecord
from dispatch.models import DispatchRecord
from logistics.models import TransportCost

class Report(models.Model):
    title = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()

    total_production_cost = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    total_dispatch_cost = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    total_logistics_cost = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    total_sales = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    total_expenses = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    profit_loss = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    def generate_report(self):
       # --- Production totals ---
        production_records = ProductionRecord.objects.filter(date__range=[self.start_date, self.end_date])
        self.total_production_cost = sum(
        (p.material_cost or 0) + (p.electricity_cost or 0) + (p.misc_cost or 0)
        for p in production_records
        )

     # --- Dispatch totals ---
        dispatch_records = DispatchRecord.objects.filter(date__range=[self.start_date, self.end_date])
        self.total_sales = sum((d.total_price or 0) for d in dispatch_records)
        self.total_dispatch_cost = self.total_sales  # assuming dispatch cost = total price (you can adjust later)

     # --- Logistics totals ---
        logistics_records = TransportCost.objects.filter(date__range=[self.start_date, self.end_date])
        self.total_logistics_cost = sum(
         (l.fuel_cost or 0) + (l.other_expenses or 0)
            for l in logistics_records
     )

        # --- Totals and Profit/Loss ---
        self.total_expenses = (
            (self.total_production_cost or 0) +
            (self.total_dispatch_cost or 0) +
            (self.total_logistics_cost or 0)
        )
        self.profit_loss = (self.total_sales or 0) - (self.total_expenses or 0)
        self.save()
