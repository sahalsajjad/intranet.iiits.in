from django.views.generic.base import TemplateView, RedirectView
from django.views.generic.edit import FormView
from django.shortcuts import resolve_url
from intranet.models import Section, Link, LeftLink, Post
from intranet.forms import LoginForm , PostForm, SuggestionForm, NewsForm, ResourceAddForm, NoticeForm
from intranet import names 
from django.conf import settings
from django.views.decorators.debug import sensitive_post_parameters
from django.utils.decorators import method_decorator
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.views import password_change, password_change_done
from django.contrib.auth.forms import PasswordChangeForm
from django.http import HttpResponseRedirect
from django.contrib import messages

class HomePageView(FormView):
	template_name = 'index.html'
	success_url = settings.LOGIN_REDIRECT_URL
	form_class = LoginForm
		
	def form_valid(self,form):
		redirect_to = settings.LOGIN_REDIRECT_URL
        	auth_login(self.request, form.get_user())
        	if self.request.session.test_cookie_worked():
           		self.request.session.delete_test_cookie()
        	return HttpResponseRedirect(redirect_to) 
	
	def form_invalid(self,form):	
		return super(HomePageView, self).form_invalid(form)
	@method_decorator(sensitive_post_parameters())	
	def dispatch(self, *args, **kwargs):
		if self.request.user.is_active:
			return HttpResponseRedirect(names.urls['posts'])
		return super(HomePageView,self).dispatch(*args, **kwargs)

	def get_context_data(self,**kwargs):
		context = super(HomePageView,self).get_context_data(**kwargs)
		context = {
			   'title':'IIIT-S Intranet',	
			   'section_items': Section.objects.order_by('-rank'),
			   'links': Link.objects.order_by('rank'),
			   'leftlinks':LeftLink.objects.order_by('rank'),
			   'pagetitle':'Home',
			   'form':LoginForm				
		}
		
		return context

class PostPageView(FormView):
	template_name = 'index.html' 
	success_url = names.urls['posts']
	form_class = PostForm
	
	def form_valid(self,form):
		redirect_to = self.success_url
		title = form.cleaned_data['title']
		content = form.cleaned_data['content']
		image = form.cleaned_data.get('image')
		print "Image" + str(image)
		if_image = True
		messages.add_message(self.request, messages.INFO, image)
		if image == None:
			if_image = False
		post = Post(title = title, 
			    content = content, 
                            image = image, 
                            author = self.request.user,
                            if_image = bool(image)
                            )
		post.save()
		return HttpResponseRedirect(redirect_to)
	def form_invalid(self,form):
		return super(PostPageView,self).form_invalid(form)

	def dispatch(self, *args, **kwargs):
		return super(PostPageView,self).dispatch(*args, **kwargs)

	def get_context_data(self, **kwargs):
		context = super(PostPageView,self).get_context_data(**kwargs)
		context = {
			   'title':'IIIT-S Intranet',	
			   'section_items': Section.objects.order_by('-rank'),
			   'links': Link.objects.order_by('rank'),
			   'leftlinks':LeftLink.objects.order_by('rank'),
			   'pagetitle':'Home',
			   'form':PostForm,
			   'posts':Post.objects.order_by('created_on')				
		} 
		return context

class NewsPageView(FormView):
	template_name = 'news.html' 
	success_url = names.urls['news']
	form_class = NewsForm
	
	def form_valid(self,Form):
		redirect_to = success_url
		return HttpResponseRedirect(redirect_to)
	def form_invalid(self,form):
		return super(NewsPageView,self).form_invalid(form)

	def dispatch(self, *args, **kwargs):
		return super(NewsPageView,self).dispatch(*args, **kwargs)

	def get_context_data(self, **kwargs):
		context = super(NewsPageView,self).get_context_data(**kwargs)
		context = {
			'':Section.objects.order_by('rank'),		
		} 
		return context


class NoticePageView(FormView):
	template_name = 'notice.html' 
	success_url = names.urls['notices']
	form_class = NoticeForm
	
	def form_valid(self,Form):
		redirect_to = success_url
		return HttpResponseRedirect(redirect_to)
	def form_invalid(self,form):
		return super(NoticePageView,self).form_invalid(form)

	def dispatch(self, *args, **kwargs):
		return super(NoticePageView,self).dispatch(*args, **kwargs)

	def get_context_data(self, **kwargs):
		context = super(NoticePageView,self).get_context_data(**kwargs)
		context = {
						
		} 
		return context


class SuggestionsPageView(FormView):
	template_name = 'suggestions.html' 
	success_url = names.urls['suggestions']
	form_class = SuggestionForm
	
	def form_valid(self,Form):
		redirect_to = success_url
		return HttpResponseRedirect(redirect_to)
	def form_invalid(self,form):
		return super(SuggestionsPageView,self).form_invalid(form)

	def dispatch(self, *args, **kwargs):
		return super(SuggestionsPageView,self).dispatch(*args, **kwargs)

	def get_context_data(self, **kwargs):
		context = super(SuggestionsPageView,self).get_context_data(**kwargs)
		context = {
						
		} 
		return context


class ResourcesPageView(FormView):
	template_name = 'resources.html' 
	success_url = names.urls['resources']
	form_class = ResourceAddForm
	
	def form_valid(self,Form):
		redirect_to = success_url
		return HttpResponseRedirect(redirect_to)
	def form_invalid(self,form):
		return super(ResourcesPageView,self).form_invalid(form)

	def dispatch(self, *args, **kwargs):
		return super(ResourcesPageView,self).dispatch(*args, **kwargs)

	def get_context_data(self, **kwargs):
		context = super(ResourcesPageView,self).get_context_data(**kwargs)
		context = {
						
		} 
		return context
