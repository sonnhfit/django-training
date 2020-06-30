from rest_framework import serializers
from .models import LopHoc, SinhVien, SinhVienLopHoc


class LopHocSerializer(serializers.ModelSerializer):
    class Meta:
        model = LopHoc
        fields = ['id', 'ma_lop', 'ten_lop']


class TestSerializer(serializers.Serializer):
    ma_lop = serializers.CharField(required=True)
    ten_lop = serializers.CharField(required=True)


class SinhvienSerializer(serializers.ModelSerializer):
    class Meta:
        model = SinhVien
        fields = ['id', 'masv', 'ho_ten', 'gioi_tinh', 'ngay_sinh']


class SinhVienLopHocSerializer(serializers.Serializer):

    gio_hoc = serializers.IntegerField()


class SinhVienLopHocMDSerializer(serializers.ModelSerializer):
    sinh_vien = SinhvienSerializer()
    lop_hoc = LopHocSerializer()
    class Meta:
        model = SinhVienLopHoc
        fields = ['id', 'gio_hoc', 'sinh_vien', 'lop_hoc']


class TinhTongSerializer(serializers.Serializer):
    a = serializers.IntegerField()
    b = serializers.IntegerField()
