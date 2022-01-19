from django import forms
from .models import Post, Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('ten', 'noi_dung')
    widgets = {
    	'ten': forms.TextInput(attrs={'class':'form-control'}),
    	'noi_dung': forms.Textarea(attrs={'class':'form-control'}),
    	}