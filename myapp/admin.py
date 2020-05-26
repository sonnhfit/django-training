from django.contrib import admin
from .models import SinhVien, LopHoc, SinhVienLopHoc, MonHoc
# Register your models here.


class SinhVienAdmin(admin.ModelAdmin):
    list_display = ('masv', 'ho_ten', 'gioi_tinh',)


admin.site.register(SinhVien, SinhVienAdmin)
admin.site.register(LopHoc)
admin.site.register(SinhVienLopHoc)
admin.site.register(MonHoc)

admin.site.site_header = 'SonNh'