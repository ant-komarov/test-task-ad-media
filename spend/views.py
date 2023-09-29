from django.db.models import Sum
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from spend.models import SpendStatistic
from spend.serializers import SpendStatisticSerializer, SpendStatisticCreateSerializer


class SpendStatisticView(APIView):
    def get(self, request):
        queryset = SpendStatistic.objects.values("date", "name").annotate(
            sum_spend=Sum("spend"),
            sum_impressions=Sum("impressions"),
            sum_clicks=Sum("clicks"),
            sum_conversion=Sum("conversion"),
            sum_revenue=Sum("revenue__revenue"),
        )
        cleaned_data = []
        for item in queryset:
            item["date"] = item["date"].strftime("%Y-%m-%d")
            cleaned_data.append(item)

        serializer = SpendStatisticSerializer(cleaned_data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = SpendStatisticCreateSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
