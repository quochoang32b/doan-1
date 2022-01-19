from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

class Post(models.Model):
    ma_post = models.CharField(max_length=50, blank=True, null=True, unique=True)
    tieu_de = models.CharField(max_length=200, unique=True, verbose_name='Tiêu đề')
    tac_gia = models.ForeignKey(User, on_delete=models.CASCADE)
    noi_dung = HTMLField()
    hinh_dai_dien = models.ImageField(null=True, blank=True, upload_to='images/')
    ngay_dang = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, null=True, blank=True, related_name='post_like')

    def number_of_likes(self):
        return self.likes.count()

    class Meta:
        ordering = ['-ngay_dang']

    def __str__(self):
        return self.tieu_de

    def get_absolute_url(self):
        return reverse('PostDetail', args=(str(self.id)))

class DoiBong(models.Model):
    ma_doi_bong = models.CharField(max_length=50, blank=True, null=True, unique=True)
    ten_doi_bong = models.CharField(max_length=50)
    logo = models.ImageField(null=True, blank=True, upload_to='images/')
    def __str__(self):
        return self.ten_doi_bong

class TranDau(models.Model):
    doi_bong = models.ManyToManyField(DoiBong, null=True, blank=True, related_name='tran_dau')
    ma_tran_dau = models.CharField(max_length=50, blank=True, null=True, unique=True)
    giai_dau = models.CharField(max_length=50)
    diem_so = models.CharField(max_length=50)
    dia_diem = models.CharField(max_length=50)
    thoi_gian = models.DateTimeField()
    trong_tai = models.CharField(max_length=50, default="Không")
    ban_thang = HTMLField(default="Không")
    pham_loi = HTMLField(default="Không")
    chien_thuat = models.ImageField(null=True, blank=True, upload_to='images/')


    def __str__(self):
        return self.ma_tran_dau


"""
class DoiHinh(models.Model):
    doi_bong = models.ForeignKey(DoiBong, null=True, blank=True, on_delete=models.CASCADE)
    ten = models.CharField(max_length=50)
    def __str__(self):
        return self.ten
"""
class CauThu(models.Model):
    doi_bong = models.ForeignKey(DoiBong, null=True, blank=True, on_delete=models.SET_NULL, related_name='cau_thu')
    ma_cau_thu = models.CharField(max_length=50, blank=True, null=True, unique=True)
    ho = models.CharField(max_length=50)
    ten = models.CharField(max_length=50)
    nam_sinh = models.DateField()
    que_quan = models.CharField(max_length=50)
    chieu_cao = models.CharField(max_length=50)
    can_nang = models.CharField(max_length=50)
    so_ao = models.CharField(max_length=50)
    vi_tri = models.CharField(max_length=50)
    so_tran = models.CharField(max_length=50)
    so_ban_thang = models.CharField(max_length=50)
    so_lan_cuu_thua = models.CharField(max_length=50)
    tieu_su = models.TextField()
    hinh_dai_dien = models.ImageField(null=True, blank=True, upload_to='images/')
    tinh_trang = models.CharField(max_length=50)
    doi_hinh = models.CharField(max_length=50, default = "Chính thức")
    def __str__(self):
        return self.ho + ' ' + self.ten


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    ten = models.CharField(max_length=50)
    noi_dung = HTMLField()
    ngay_dang = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.post.tieu_de, self.ten)

