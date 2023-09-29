from django.urls import path

from spend.views import SpendStatisticView

urlpatterns = [path("", SpendStatisticView.as_view(), name="spend")]

app_name = "spend"
