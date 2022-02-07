from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, FormView
from django.views.generic.detail import SingleObjectMixin
from .models import Post, CauThu, DoiBong, TranDau, Comment
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from .forms import CommentForm
# Create your views here.
#def home(request):
 #   return render(request, 'daihuu/home.html')

def HomeView(request):
    some_post = Post.objects.all().order_by("-ngay_dang")[0:6]
    some_match = TranDau.objects.all().order_by("-thoi_gian")
    some_team = DoiBong.objects.all()
    return render(request, 'daihuu/home.html', {'some_post': some_post, 'some_match': some_match,'some_team':some_team})

class TinTucView(ListView):
    model = Post
    template_name = "daihuu/tintuc.html"
    context_object_name = 'posts'

def PostDetailView(request, pk):
    some_post_detail = Post.objects.filter(id = pk)
    likes_connected = get_object_or_404(Post, id=pk)
    liked = False
    if likes_connected.likes.filter(id=request.user.id).exists():
        liked = True
    number_of_likes = likes_connected.number_of_likes()
    post_is_liked = liked
    post = Post.objects.get(id = pk)
    comments = post.comments.all

    if request.method == 'POST':
        cf = CommentForm(request.POST or None)
        if cf.is_valid():
            noi_dung = request.POST.get('noi_dung')
            comment = Comment.objects.create(post = post, ten = request.user, noi_dung = noi_dung)
            comment.save()
            return HttpResponseRedirect(reverse('PostDetail', kwargs={'pk': post.id}))
    else:
        cf = CommentForm()
    return render(request,'daihuu/post_detail.html',{'some_post_detail':some_post_detail,'number_of_likes':number_of_likes,'post_is_liked':post_is_liked,'comment_form':cf,'comments': comments})
    """
    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        likes_connected = get_object_or_404(Post, id=self.kwargs['pk'])
        liked = False
        if likes_connected.likes.filter(id=self.request.user.id).exists():
            liked = True
        data['number_of_likes'] = likes_connected.number_of_likes()
        data['post_is_liked'] = liked
        return data
    """
"""
    def get_absolute_url(self):
        return reverse('PostDetail', args=[str(self.pk)])

    def get(self, request, *args, **kwargs):
        view = PostDisplay.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = PostComment.as_view()
        return view(request, *args, **kwargs)
"""

"""
class PostDisplay(DetailView):
    model = Post
    template_name = 'daihuu/post_detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        likes_connected = get_object_or_404(Post, id=self.kwargs['pk'])
        liked = False
        if likes_connected.likes.filter(id=self.request.user.id).exists():
            liked = True
        context['number_of_likes'] = likes_connected.number_of_likes()
        context['post_is_liked'] = liked
        context['form'] = CommentForm()
        return context
"""

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

def ChinhThucView(request):
    #pkdoibong = DoiBong.objects.get(ma_doi_bong="daihuu").pk
    #some_cauthu = CauThu.objects.filter(doi_bong=pkdoibong)
    some_cauthu = CauThu.objects.filter(doi_bong__ma_doi_bong="daihuu").filter(doi_hinh="Chính thức")
    thumon = some_cauthu.filter(vi_tri="Thủ môn")
    hauve = some_cauthu.filter(vi_tri="Hậu vệ")
    tienve = some_cauthu.filter(vi_tri="Tiền vệ")
    tiendao = some_cauthu.filter(vi_tri="Tiền đạo")
    return render(request, 'daihuu/chinhthuc.html', {'some_cauthu': some_cauthu, 'thumon':thumon, 'hauve':hauve, 'tienve': tienve, 'tiendao': tiendao})

def DuBiView(request):
    #pkdoibong = DoiBong.objects.get(ma_doi_bong="daihuu").pk
    #some_cauthu = CauThu.objects.filter(doi_bong=pkdoibong)
    some_cauthu = CauThu.objects.filter(doi_bong__ma_doi_bong="daihuu").filter(doi_hinh="Dự bị")
    thumon = some_cauthu.filter(vi_tri="Thủ môn")
    hauve = some_cauthu.filter(vi_tri="Hậu vệ")
    tienve = some_cauthu.filter(vi_tri="Tiền vệ")
    tiendao = some_cauthu.filter(vi_tri="Tiền đạo")
    return render(request, 'daihuu/dubi.html', {'some_cauthu': some_cauthu, 'thumon':thumon, 'hauve':hauve, 'tienve': tienve, 'tiendao': tiendao})

def LichThiDauView(request):
    some_match_lich = TranDau.objects.all().order_by("-thoi_gian")
    return render(request, 'daihuu/lichthidau.html', {'ds_trandau': some_match_lich})

def LichThiDauDetailView(request,pk):
    some_match_thi_dau = TranDau.objects.filter(id = pk)
    #daihuu = CauThu.objects.filter(doi_bong__ma_doi_bong="daihuu").filter(doi_hinh="Chính thức")
    team1 = some_match_thi_dau.first().doi_bong.all().first().cau_thu.filter(doi_hinh="Chính thức")
    team2 = some_match_thi_dau.first().doi_bong.all().last().cau_thu.filter(doi_hinh="Chính thức")
    return render(request,'daihuu/lichthidau_detail.html',{'team1':team1,'team2':team2,'some_match_thi_dau':some_match_thi_dau})

"""
class AddCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = "daihuu/add_comment.html"
    #fields = '__all__'
    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)
    success_url = reverse_lazy('TinTuc')
"""

"""
class PostComment(SingleObjectMixin, FormView):
    model = Post
    form_class = CommentForm
    template_name = 'daihuu/post_detail.html'

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super(PostComment, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.post = self.object
        comment.save()
        return super().form_valid(form)

    def get_success_url(self):
        post = self.get_object()
        return reverse('PostDetail', kwargs={'pk': post.pk}) + '#comments'
"""