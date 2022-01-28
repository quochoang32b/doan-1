from django.contrib import admin
from .models import Post, DoiBong, CauThu, TranDau, Comment
# Register your models here

class CommentInline(admin.StackedInline):
    model = Comment
    extra = 0
    ordering = ('-ngay_dang',)


class PostAdmin(admin.ModelAdmin):
    list_display = ('tieu_de', 'tac_gia', 'ngay_dang')
    search_fields = ['tieu_de', 'noi_dung']
    inlines = [
        CommentInline,
    ]


admin.site.register(Post, PostAdmin)
admin.site.register(DoiBong)
admin.site.register(CauThu)
admin.site.register(TranDau)
admin.site.register(Comment)
