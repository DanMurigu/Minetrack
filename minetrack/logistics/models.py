from django.db import models
from django.conf import settings
from django.core.validators import RegexValidator


# Create your models here.
class TransportCost(models.Model): #calculates cost of product distribution
    logistics = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)
    driver = models.TextField(max_length=200)
    vehicle_no = models.CharField(max_length=100, validators=[RegexValidator(regex='^[A-Za-z0-9]+$')])
    fuel_cost = models.DecimalField(max_digits=10, decimal_places=2)
    other_expenses = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    @property
    def total_expense(self):
        return self.fuel_cost + self.other_expenses
    
    def __str__(self):
        return f"Trip by {self.driver} on {self.date} costing {self.total_expense}"
