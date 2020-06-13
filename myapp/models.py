from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class SinhVien(models.Model):
    masv = models.CharField(unique=True, max_length=200, verbose_name='Mã sinh viên')
    ho_ten = models.CharField(max_length=200, default='', verbose_name='Họ tên')
    gioi_tinh = models.BooleanField(default=False, verbose_name='Giới tính')
    ngay_sinh = models.DateField(null=True, blank=True)

    @property
    def get_year(self):
        return self.ngay_sinh


    def __str__(self):
        return self.ho_ten

    class Meta:
        verbose_name = 'Sinh Viên'
        verbose_name_plural = 'Sinh Viên'


class LopHoc(models.Model):
    ma_lop = models.CharField(unique=True, max_length=200)
    ten_lop = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return str(self.id)


class SinhVienLopHoc(models.Model):
    sinh_vien = models.ForeignKey(SinhVien, on_delete=models.CASCADE)
    lop_hoc = models.ForeignKey(LopHoc, on_delete=models.CASCADE)
    gio_hoc = models.IntegerField(default=7)


class MonHoc(models.Model):
    code = models.CharField(primary_key=True, max_length=200)
    year = models.CharField(max_length=200, unique=True)
    ten_mon = models.CharField(max_length=255)
    lop = models.ForeignKey(LopHoc, on_delete=models.CASCADE)


