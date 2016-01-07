from django import forms
from django.contrib.postgres.forms import SimpleArrayField
from django.contrib.auth.forms import AuthenticationForm
class CommentForm(forms.Form):
	comment = forms.CharField(widget = forms.Textarea)	 

class LoginForm(AuthenticationForm):
	username = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control',
								 'placeholder':'Enter your Email', 				
								}))	 
	password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control',
								     'placeholder':'Enter your password',			
								}))

class NewsForm(forms.Form):
	title = forms.CharField()
	content = forms.CharField()
	image = forms.ImageField()
	file_upload = forms.FileField()
	mail_list = forms.CharField()
	
	
class NoticeForm(forms.Form):
	title = forms.CharField()
	description = forms.CharField()
	mail_list = forms.CharField()
	file_upload = forms.FileField()
	
	
class PostForm(forms.Form):
	title = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 
							      'placeholder':'What\'s the title of this post ?',	
							}))
	content = forms.CharField(widget=forms.Textarea(attrs={ 'class':'form-control',
								'placeholder':'What\'s the post about ? ...',
								'rows':'5'
						}))
	image = forms.ImageField(widget=forms.ClearableFileInput(attrs={
								'class':'form-control file'	
						}), required=False)
	
		
class ResourceAddForm(forms.Form):
	title = forms.CharField()
	file_upload = forms.FileField()
	
class SuggestionForm(forms.Form):
	suggestion = forms.CharField()	

