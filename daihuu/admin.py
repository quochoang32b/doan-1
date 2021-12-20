from django.contrib import admin
from .models import Post, DoiBong, CauThu, TranDau
# Register your models here
class PostAdmin(admin.ModelAdmin):
    list_display = ('tieu_de', 'tac_gia', 'ngay_dang')
    search_fields = ['tieu_de', 'noi_dung']


admin.site.register(Post, PostAdmin)
admin.site.register(DoiBong)
admin.site.register(CauThu)
admin.site.register(TranDau)
