from django.http import JsonResponse
import json
from intranet.models import Comment, Post

def post_comment(request):
	if request.method == 'POST':
		
		comment = request.POST['comment']
		parent_post = int(self.request.POST['parent_post_id'])
		parent_post = Post.objects.get(id=parent_post) 
		comment_object = Comment(comment=comment, author=self.request.user, post = parent_post)
		comment_object.save()
		response_data = {}
		response_data['comment_new']=comment_object
		response = json.dumps(response_data)

		return JsonResponse(response, content_type=application/json)
