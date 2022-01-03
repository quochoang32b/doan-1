from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Post, CauThu, DoiBong, TranDau
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.
#def home(request):
 #   return render(request, 'daihuu/home.html')

def HomeView(request):
    some_post = Post.objects.all().order_by("-ngay_dang")[0:3]
    some_match = TranDau.objects.all().order_by("-thoi_gian")
    some_team = DoiBong.objects.all()
    ds1=[]
    for i in TranDau.objects.all():
        for j in DoiBong.objects.filter(tran_dau__id=i.id).order_by("-id"):
            ds1.append(j.logo.url)
    return render(request, 'daihuu/home.html', {'some_post': some_post, 'some_match': some_match,'some_team':some_team, 'table_doi_bong':DoiBong, 'table_tran_dau':TranDau, 'ds1': ds1})

class TinTucView(ListView):
    model = Post
    template_name = "daihuu/tintuc.html"

class PostDetailView(DetailView):
    model = Post
    template_name = "daihuu/post_detail.html"

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        likes_connected = get_object_or_404(Post, id=self.kwargs['pk'])
        liked = False
        if likes_connected.likes.filter(id=self.request.user.id).exists():
            liked = True
        data['number_of_likes'] = likes_connected.number_of_likes()
        data['post_is_liked'] = liked
        return data

def PostLike(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    return HttpResponseRedirect(reverse('PostDetail', args=[str(pk)]))


def ThongTinView(request):
    return render(request, "daihuu/thongtin.html")

def DoiHinhView(request):
    #pkdoibong = DoiBong.objects.get(ma_doi_bong="daihuu").pk
    #some_cauthu = CauThu.objects.filter(doi_bong=pkdoibong)
    some_cauthu = CauThu.objects.filter(doi_bong__ma_doi_bong="daihuu")
    thumon = some_cauthu.filter(vi_tri="Thủ môn")
    hauve = some_cauthu.filter(vi_tri="Hậu vệ")
    tienve = some_cauthu.filter(vi_tri="Tiền vệ")
    tiendao = some_cauthu.filter(vi_tri="Tiền đạo")
    return render(request, 'daihuu/doihinh.html', {'some_cauthu': some_cauthu, 'thumon':thumon, 'hauve':hauve, 'tienve': tienve, 'tiendao': tiendao})

class DoiHinhDetailView(DetailView):
    model = CauThu
    template_name = "daihuu/doihinh_detail.html"

def LichThiDauView(request):
    some_match_lich = TranDau.objects.all().order_by("-thoi_gian")
    danh_sach = []
    for i in TranDau.objects.all():
        for j in DoiBong.objects.filter(tran_dau__id=i.id).order_by("-id"):
            danh_sach.append(j.logo.url)
    return render(request, 'daihuu/lichthidau.html', {'ds_trandau': some_match_lich, 'ds': danh_sach})
