from django.shortcuts import render
from django.views import View
from .models import SinhVien
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from .models import LopHoc, SinhVienLopHoc
from .serializers import (LopHocSerializer, TestSerializer,
                          SinhVienLopHocSerializer, SinhVienLopHocMDSerializer, TinhTongSerializer)
from rest_framework import status
# Create your views here.



def index(request):
    return render(request, 'index.html')


class IndexView(View):

    def get(self, request):
        list_sv = SinhVien.objects.all()
        sv = SinhVien.objects.get(id=1)

        context = {
            'var1': 'nguyen huu son',
            'var2': 224,
            'list_sv': list_sv,
            'sinh_vien': sv
        }
        return render(request, 'index.html', context)


class GetClass(APIView):
    permission_classes = (AllowAny, )

    def get(self, request):
        lh = LopHoc.objects.all()
        da = LopHocSerializer(lh, many=True)
        return Response(da.data)

    def post(self, request):
        a = TestSerializer(data=request.data)
        if a.is_valid():
            print()
            lop = LopHoc(ma_lop=a.data['ma_lop'], ten_lop=a.data['ma_lop'])
            lop.save()
            return Response("lop {0} da duoc tao".format(str(lop.id)), status=status.HTTP_200_OK)
        else:
            return Response("bad request", status=status.HTTP_400_BAD_REQUEST)


class HelloView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': 'Hello {0}, World!'.format(request.user.username)}
        return Response(content)
# JWT


class GetSinhVienLopHoc(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, id_sv_lh):
        svlh = SinhVienLopHoc.objects.get(id=id_sv_lh)

        data = SinhVienLopHocMDSerializer(instance=svlh)

        return Response(data=data.data, status=status.HTTP_200_OK)

    def post(self, request):
        pass

    def delete(self, request):
        pass

    def put(self, request):
        pass



class TinhTong(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        tinhtongser = TinhTongSerializer(data=request.data)

        if not tinhtongser.is_valid():
            return Response('sai du lieu', status=status.HTTP_400_BAD_REQUEST)

        a = tinhtongser.data['a']
        b = tinhtongser.data['b']

        c = int(a) + int(b)

        data = {
            'ketqua': c
        }

        return Response(data=data, status=status.HTTP_200_OK)


class APIGiongFacebook(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        data = {
          "name": "Nguyễn Sơn",
          "id": "1014028002074112"
        }
        return Response(data=data, status=status.HTTP_200_OK)
