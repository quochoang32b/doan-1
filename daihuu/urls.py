from django.urls import path, include
from .views import HomeView, PostDetailView, ThongTinView, DoiHinhDetailView, TinTucView, DoiHinhView, ChinhThucView, DuBiView, PostLike, LichThiDauDetailView, TinTucTheLoaiView, HoatDongView
from . import views
urlpatterns = [
    #path('', views.home, name="home"),
    path('', views.HomeView, name="Home"),
    path('post/<int:pk>', PostDetailView, name="PostDetail"),
    path('thongtin', ThongTinView, name="ThongTin"),
    path('doihinh', DoiHinhView, name="DoiHinh"),
    path('chinhthuc', ChinhThucView, name="ChinhThuc"),
    path('dubi', DuBiView, name="DuBi"),
    path('doihinh/<int:pk>', DoiHinhDetailView.as_view(), name="DoiHinhDetail"),
    path('tintuc', TinTucView, name="TinTuc"),
    path('tintuc/<str:tl>', TinTucTheLoaiView, name="TinTucTheLoai"),
    path('hoatdong', HoatDongView, name="HoatDong"),
    path('lichthidau', views.LichThiDauView, name="LichThiDau"),
    path('lichthidau/<int:pk>', views.LichThiDauDetailView, name="LichThiDauDetail"),
    path('post-like/<int:pk>', views.PostLike, name="LikePost"),
]
