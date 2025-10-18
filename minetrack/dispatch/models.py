from django.db import models
from django.conf import settings

# Create your models here.
class DispatchRecord(models.Model): #calculates the sales revenue
    dispatcher = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    tons_dispatched = models.DecimalField(max_digits=10, decimal_places=2)
    cost_of_tons = models.DecimalField(max_digits=10, decimal_places=2)

    @property
    def total_price(self):
        return self.tons_dispatched * self.cost_of_tons
    
    def __str__(self):
        return f"Dispatch {self.date} by {self.dispatcher.username} costing {self.total_price}"
    