"""
URL configuration for minetrack project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from dispatch.views import DispatchRecordViewSet
from production.views import ProductionRecordViewSet
from logistics.views import TransportCostViewSet

router = routers.DefaultRouter()
router.register(r'dispatch/records', DispatchRecordViewSet)
router.register(r'production/records', ProductionRecordViewSet)
router.register(r'logistics/trips', TransportCostViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),   
    path('api/reports/', include('reports.urls')),
    path('reports/', include('reports.urls')),
]

