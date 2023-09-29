from django.db.models import Sum
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from revenue.models import RevenueStatistic
from revenue.serializers import (
    RevenueStatisticSerializer,
    RevenueStatisticCreateSerializer,
)


class RevenueStatisticView(APIView):
    def get(self, request):
        queryset = RevenueStatistic.objects.values("date", "name").annotate(
            sum_revenue=Sum("revenue"),
            sum_spend=Sum("spend__spend"),
            sum_impressions=Sum("spend__impressions"),
            sum_clicks=Sum("spend__clicks"),
            sum_conversion=Sum("spend__conversion"),
        )
        cleaned_data = []
        for item in queryset:
            item["date"] = item["date"].strftime("%Y-%m-%d")
            cleaned_data.append(item)

        serializer = RevenueStatisticSerializer(cleaned_data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = RevenueStatisticCreateSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
