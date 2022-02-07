from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

class Post(models.Model):
    ma_post = models.CharField(max_length=50, blank=True, null=True, unique=True, verbose_name='Mã post')
    tieu_de = models.CharField(max_length=200, unique=True, verbose_name='Tiêu đề')
    tac_gia = models.ForeignKey(User, verbose_name='Tác giả', on_delete=models.CASCADE)
    noi_dung = HTMLField( verbose_name='Nội dung')
    hinh_dai_dien = models.ImageField(null=True, blank=True, upload_to='images/', verbose_name='Hình đại diện')
    ngay_dang = models.DateTimeField(auto_now_add=True, verbose_name='Ngày đăng')
    likes = models.ManyToManyField(User, null=True, blank=True, related_name='post_like', verbose_name='Người like')

    def number_of_likes(self):
        return self.likes.count()

    class Meta:
        ordering = ['-ngay_dang']
        verbose_name = 'Tin tức'
        verbose_name_plural = 'Tin tức'

    def __str__(self):
        return self.tieu_de

    #def get_absolute_url(self):
     #   return reverse('PostDetail', args=(str(self.id)))

class DoiBong(models.Model):
    ma_doi_bong = models.CharField(max_length=50, blank=True, null=True, unique=True, verbose_name='Mã đội bóng')
    ten_doi_bong = models.CharField(max_length=50, verbose_name='Tên đội bóng')
    logo = models.ImageField(null=True, blank=True, upload_to='images/', verbose_name='Logo đội bóng')

    class Meta:
        verbose_name = 'Đội bóng'
        verbose_name_plural = 'Đội bóng'

    def __str__(self):
        return self.ten_doi_bong

class TranDau(models.Model):
    doi_bong = models.ManyToManyField(DoiBong, null=True, blank=True, related_name='tran_dau', verbose_name='Đội bóng')
    ma_tran_dau = models.CharField(max_length=50, blank=True, null=True, unique=True, verbose_name='Mã trận đấu')
    giai_dau = models.CharField(max_length=50, verbose_name='Giải đấu')
    diem_so = models.CharField(max_length=50, verbose_name='Điểm số')
    dia_diem = models.CharField(max_length=50, verbose_name='Địa điểm')
    thoi_gian = models.DateTimeField( verbose_name='Thời gian')
    trong_tai = models.CharField(max_length=50, default="TBD", verbose_name='Trọng tài')
    ban_thang = HTMLField(default="TBD", verbose_name='Bàn thắng')
    pham_loi = HTMLField(default="TBD", verbose_name='Phạm lỗi')
    chien_thuat = models.ImageField(null=True, blank=True, upload_to='images/', verbose_name='Chiến thuật')

    class Meta:
        ordering = ['-thoi_gian']
        verbose_name = 'Trận đấu'
        verbose_name_plural = 'Trận đấu'

    def __str__(self):
        return self.giai_dau + ' - ' + self.ma_tran_dau


"""
class DoiHinh(models.Model):
    doi_bong = models.ForeignKey(DoiBong, null=True, blank=True, on_delete=models.CASCADE)
    ten = models.CharField(max_length=50)
    def __str__(self):
        return self.ten
"""
class CauThu(models.Model):
    doi_bong = models.ForeignKey(DoiBong, null=True, blank=True, on_delete=models.SET_NULL, related_name='cau_thu', verbose_name='Đội bóng')
    ma_cau_thu = models.CharField(max_length=50, blank=True, null=True, unique=True, verbose_name='Mã cầu thủ')
    ho = models.CharField(max_length=50, verbose_name='Họ')
    ten = models.CharField(max_length=50, verbose_name='Tên')
    nam_sinh = models.DateField(verbose_name='Năm sinh')
    que_quan = models.CharField(max_length=50, verbose_name='Quê quán')
    chieu_cao = models.CharField(max_length=50, verbose_name='Chiều cao')
    can_nang = models.CharField(max_length=50, verbose_name='Cân nặng')
    so_ao = models.CharField(max_length=50, verbose_name='Số áo')
    vi_tri = models.CharField(max_length=50, verbose_name='Vị trí')
    so_tran = models.CharField(max_length=50, verbose_name='Số trận')
    so_ban_thang = models.CharField(max_length=50, verbose_name='Số bàn thắng')
    so_lan_cuu_thua = models.CharField(max_length=50, verbose_name='Số lần cứu thua')
    tieu_su = models.TextField(verbose_name='Tiểu sử')
    hinh_dai_dien = models.ImageField(null=True, blank=True, upload_to='images/', verbose_name='Hình đại diện')
    tinh_trang = models.CharField(max_length=50, verbose_name='Tình trạng')
    doi_hinh = models.CharField(max_length=50, default = "Chính thức", verbose_name='Đội hình')

    class Meta:
        ordering = ['-doi_bong']
        verbose_name = 'Cầu thủ'
        verbose_name_plural = 'Cầu thủ'

    def __str__(self):
        return self.ho + ' ' + self.ten + ' - ' + self.doi_bong.ten_doi_bong


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE, verbose_name='Bài viết')
    ten = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Người bình luận')
    noi_dung = HTMLField(verbose_name='Nội dung')
    ngay_dang = models.DateTimeField(auto_now_add=True, verbose_name='Ngày đăng')

    class Meta:
        verbose_name = 'Bình luận'
        verbose_name_plural = 'Bình luận'

    def __str__(self):
        return '%s - %s - %s' % (self.post.tieu_de, self.ten, self.noi_dung)

