from django import forms
from .models import Post, Comment

class CommentForm(forms.ModelForm):
    noi_dung = forms.CharField(label ="Nội dung",widget = forms.Textarea(
    attrs ={
        'class':'form-control',
        'rows':5,
        'cols':100,
    }))
    class Meta:
        model = Comment
        fields = ['noi_dung']

    #def __init__(self, *args, **kwargs):
     #   """Save the request with the form so it can be accessed in clean_*()"""
      #  self.request = kwargs.pop('request', None)
       # super(CommentForm, self).__init__(*args, **kwargs)
    