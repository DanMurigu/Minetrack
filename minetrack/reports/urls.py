from django.urls import path
from . import views

urlpatterns = [
    path('generate/', views.generate_report, name='generate_report'),
    path('summary/<int:report_id>/', views.report_summary, name='report_summary'),
]


