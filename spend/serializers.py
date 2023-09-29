from rest_framework import serializers

from spend.models import SpendStatistic


class SpendStatisticSerializer(serializers.Serializer):
    date = serializers.DateField()
    name = serializers.CharField(max_length=255)
    sum_spend = serializers.DecimalField(max_digits=10, decimal_places=2)
    sum_impressions = serializers.IntegerField()
    sum_clicks = serializers.IntegerField()
    sum_conversion = serializers.IntegerField()
    sum_revenue = serializers.DecimalField(max_digits=9, decimal_places=2)


class SpendStatisticCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpendStatistic
        fields = "__all__"
