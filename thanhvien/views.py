from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.urls import reverse_lazy
from .forms import SignUpForm, EditProfileForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
# Create your views here.

"""
def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ("Thành công"))
            return redirect('Home')
            # Redirect to a success page.
        else:
            messages.success(request, ("Lỗi đăng nhập"))
            return redirect('login')
            # Return an 'invalid login' error message.
    else:
        return render(request, 'registration/login.html')
"""
class UserRegisterView(SuccessMessageMixin, generic.CreateView):
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')
    success_message = "Tạo tài khoản thành công !"

class UserEditView(SuccessMessageMixin, generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('edit_profile')
    success_message = "Cập nhật tài khoản thành công !"

    def get_object(self):
        return self.request.user

class SuccessMessageMixin:
    """
    Add a success message on successful form submission.
    """
    success_message = ''

    def form_valid(self, form):
        response = super().form_valid(form)
        success_message = self.get_success_message(form.cleaned_data)
        if success_message:
            messages.success(self.request, success_message)
        return response

    def get_success_message(self, cleaned_data):
        return self.success_message % cleaned_data
"""
def register(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, "Tạo thành công")
            return redirect('Home')
    else:
        form = SignUpForm()
    return render(request, 'registration/register.html',{'form':form})
"""