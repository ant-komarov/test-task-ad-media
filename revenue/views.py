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

        serializer = RevenueStatisticSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = RevenueStatisticCreateSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
