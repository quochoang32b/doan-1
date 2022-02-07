from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class SignUpForm(UserCreationForm):
	email = forms.EmailField(widget=forms.EmailInput(attrs ={'class':'form-control',}))
	first_name = forms.CharField(label ="Tên",widget = forms.TextInput(attrs ={'class':'form-control',}))
	last_name = forms.CharField(label ="Họ",widget = forms.TextInput(attrs ={'class':'form-control',}))

	class Meta:
		model = User
		fields = ['username', 'last_name','first_name','email','password1','password2']

	def __init__(self, *args, **kwargs):
		super(SignUpForm, self).__init__(*args, **kwargs)
		for fieldname in ['username', 'password1', 'password2']:
			self.fields[fieldname].help_text = None
		self.fields['username'].widget.attrs['class'] = 'form-control'
		self.fields['password1'].widget.attrs['class'] = 'form-control'
		self.fields['password2'].widget.attrs['class'] = 'form-control'
