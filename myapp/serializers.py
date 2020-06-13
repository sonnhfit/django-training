from rest_framework import serializers
from .models import LopHoc


class LopHocSerializer(serializers.ModelSerializer):
    class Meta:
        model = LopHoc
        fields = ['id', 'ma_lop', 'ten_lop']


class TestSerializer(serializers.Serializer):
    ma_lop = serializers.CharField(required=True)
    ten_lop = serializers.CharField(required=True)
