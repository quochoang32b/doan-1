from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post, CauThu, DoiBong, TranDau

# Create your views here.
#def home(request):
 #   return render(request, 'daihuu/home.html')

def HomeView(request):
    some_post = Post.objects.all().order_by("-ngay_dang")[0:2]
    some_match = TranDau.objects.all().order_by("-thoi_gian")
    some_team = DoiBong.objects.all()
    ds=list()
    for i in TranDau.objects.all():
        for j in DoiBong.objects.filter(trandau=i):
            ds.append(j.logo.url)

    return render(request, 'daihuu/home.html', {'some_post': some_post, 'some_match': some_match,'some_team':some_team, 'table_doi_bong':DoiBong, 'table_tran_dau':TranDau, 'ds': ds})

class TinTucView(ListView):
    model = Post
    template_name = "daihuu/tintuc.html"

class PostDetailView(DetailView):
    model = Post
    template_name = "daihuu/post_detail.html"

def ThongTinView(request):
    return render(request, "daihuu/thongtin.html")

def DoiHinhView(request):
    #pkdoibong = DoiBong.objects.get(ma_doi_bong="daihuu").pk
    #some_cauthu = CauThu.objects.filter(doi_bong=pkdoibong)
    some_cauthu = CauThu.objects.filter(doi_bong__ma_doi_bong="daihuu")
    return render(request, 'daihuu/doihinh.html', {'some_cauthu': some_cauthu})

class DoiHinhDetailView(DetailView):
    model = CauThu
    template_name = "daihuu/doihinh_detail.html"

def LichThiDauView(request):
    some_match = TranDau.objects.all().order_by("-thoi_gian")
    some_team = DoiBong.objects.all()
    ds = list()
    for i in TranDau.objects.all():
        for j in DoiBong.objects.filter(trandau=i):
            ds.append(j.logo.url)
    return render(request, 'daihuu/lichthidau.html', {'some_match': some_match, 'some_team': some_team, 'table_doi_bong': DoiBong,'table_tran_dau': TranDau, 'ds': ds})
