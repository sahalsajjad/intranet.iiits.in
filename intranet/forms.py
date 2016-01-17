from django import forms
from django.contrib.postgres.forms import SimpleArrayField
from django.contrib.auth.forms import AuthenticationForm
class CommentForm(forms.Form):
	comment = forms.CharField(widget = forms.Textarea(attrs={'class':'form-control',
								 'placeholder':'Comment Here...',
								 'rows':'1',
								 'id':'comment-text'							 				
								}))	 

class LoginForm(AuthenticationForm):
	username = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control',
								 'placeholder':'Enter your Email', 				
								}))	 
	password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control',
								     'placeholder':'Enter your password',			
								}))

class NewsForm(forms.Form):
	title = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control',
								 'placeholder':'What\'s the title of the news', 				
								}))
	content = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control',
								 'placeholder':'What\'s the news about', 				
								}))
	image = forms.ImageField(widget=forms.FileInput(attrs={'class':'form-control',
								 'placeholder':'Upload an Image (optional)', 				
								}),required=False)
	file_upload = forms.FileField(widget=forms.FileInput(attrs={'class':'form-control',
								 'placeholder':'Choose a file (optional)', 				
								}),required=False)
	mail_list = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control',
								 'placeholder':'List of emails to mail this news (optional)', 				
								}),required=False)
	
	
class NoticeForm(forms.Form):
	title = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control',
                                                              'placeholder':'Please provide the title of Notice' 				
								}))
	description = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control',
                                                              'placeholder':'What\'s the notice about' 					
								}))
	mail_list = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control',
                                                              'placeholder':'List of emails to mail this   Notice' 				
								}), required=False)
	file_upload = forms.FileField(widget=forms.FileInput(attrs={'class':'form-control',
                                                              'placeholder':'Upload a file(optional)'						
								}), required = False)
	
	
class PostForm(forms.Form):
	title = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 
							      'placeholder':'What\'s the title of this post ?',	
							}))
	content = forms.CharField(widget=forms.Textarea(attrs={ 'class':'form-control',
								'placeholder':'What\'s the post about ? ...',
								'rows':'5'
						}))
	image = forms.ImageField(widget=forms.FileInput(attrs={
								'class':'file',
								'label':'Upload an Image'	
						}), required=False)
	
		
class ResourceAddForm(forms.Form):
	title = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 
							      'placeholder':'What\'s the name of this resource file ?',	
							}))
	file_upload = forms.FileField(widget=forms.FileInput(attrs={
								'class':'form-control file'	
						}), required=True)
	
class SuggestionForm(forms.Form):
	suggestion = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control',
                                                              'placeholder':'Please add your valuable suggestion' 				
								}))	


