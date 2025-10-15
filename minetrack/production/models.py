from django.db import models
from django.conf import settings

# Create your models here.
class ProductionRecord(models.Model): #Calculates the total cost of production
    production = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    material_cost = models.DecimalField(max_digits=10, decimal_places=2)
    electricity_cost = models.DecimalField(max_digits=10, decimal_places=2)
    misc_cost = models.DecimalField(max_digits=10, decimal_places=2)

    @property
    def total_production_cost(self):
        return self.material_cost + self.electricity_cost + self.misc_cost
    
    def __str__(self):
        return f"Production on {self.date} costing {self.total_production_cost}"