from django.contrib import admin
from .models import Post, DoiBong, CauThu, TranDau, Comment
# Register your models here

class CommentInline(admin.StackedInline):
    model = Comment
    extra = 0
    ordering = ('-ngay_dang',)


class PostAdmin(admin.ModelAdmin):
    list_display = ('ma_post','tieu_de','the_loai','tac_gia','ngay_dang')
    search_fields = ['tieu_de', 'noi_dung']
    inlines = [
        CommentInline,
    ]

class CauthuInline(admin.StackedInline):
    model = CauThu
    extra = 0

class DoiBongAdmin(admin.ModelAdmin):
    inlines = [
        CauthuInline,
    ]

class TranDauAdmin(admin.ModelAdmin):
    list_display = ('ma_tran_dau','giai_dau','thoi_gian')
    search_fields = ['giai_dau', 'ma_tran_dau', 'doi_bong__ten_doi_bong']

class CauThuAdmin(admin.ModelAdmin):
    search_fields = ['ho', 'ten', 'doi_bong__ten_doi_bong']

class CommentAdmin(admin.ModelAdmin):
    search_fields = ['ten__username', 'post__tieu_de']


admin.site.register(Post, PostAdmin)
admin.site.register(DoiBong, DoiBongAdmin)
admin.site.register(CauThu, CauThuAdmin)
admin.site.register(TranDau, TranDauAdmin)
admin.site.register(Comment, CommentAdmin)
