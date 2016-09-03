from django.contrib.auth.forms import AuthenticationForm 
from django import forms
from .models import Blog
# If you don't do this you cannot use Bootstrap CSS
class NewBlog(forms.ModelForm):
	title = forms.CharField(max_length = 250)
	body = forms.CharField(widget=forms.Textarea)
	show = forms.BooleanField(required=False)

	class Meta:
		model = Blog
		fields = [
		'title',
		'body',
		'show',
		]
	def clean(self,*agrs,**kwargs):
		title = self.cleaned_data.get("title")
		body = self.cleaned_data.get("body")
		return super(NewBlog,self).clean(*agrs,**kwargs)