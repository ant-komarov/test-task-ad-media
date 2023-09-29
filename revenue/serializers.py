from rest_framework import serializers

from revenue.models import RevenueStatistic


class RevenueStatisticSerializer(serializers.Serializer):
    date = serializers.DateField()
    name = serializers.CharField(max_length=255)
    total_revenue = serializers.DecimalField(max_digits=9, decimal_places=2)
    total_spend = serializers.DecimalField(max_digits=10, decimal_places=2)
    total_impressions = serializers.IntegerField()
    total_clicks = serializers.IntegerField()
    total_conversion = serializers.IntegerField()


class RevenueStatisticCreateSerializer(serializers.Serializer):
    class Meta:
        model = RevenueStatistic
        fields = "__all__"
