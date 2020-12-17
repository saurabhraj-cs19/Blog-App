from django import forms 
from .models import *

# Create your forms here.
class PostForm(forms.ModelForm):	

	class Meta:

		model = Post 
		fields = ['title', 'content']
		style = { 
			'class': 'form-control',
			'required': True
		}
		widgets = {
			'title': forms.TextInput(attrs=style),
			'content': forms.Textarea(attrs=style),
		}


class CommentForm(forms.ModelForm):

	class Meta:
		model = Comment 
		fields = ['content']
		style = { 
			'class': 'form-control',
			'required': True
		}
		widgets = { 'content': forms.Textarea(attrs=style) }


class ReplyForm(forms.ModelForm):

	class Meta:
		model = Reply
		fields = ['content']
		style = { 
			'class': 'form-control',
			'required': True
		}
		widgets = { 'content': forms.Textarea(attrs=style) }