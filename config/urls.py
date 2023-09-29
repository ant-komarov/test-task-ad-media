from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("spend/", include("spend.urls", namespace="spend")),
    path("revenue/", include("revenue.urls", namespace="revenue")),
]
