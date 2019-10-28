from django.shortcuts import render
from .models import Post
from APIServer.models import contest

def PostList(req):
	data = Post.objects.filter(status = 1).order_by('-created_on')
	contestList = contest.objects.all()
	completeData = {
		'posts' : data,
		'contestList' : contestList,
	}
	return render(req, "index.html", completeData)

def PostDetail(req, slug):
	post = Post.objects.get(status=1, slug=slug)
	contestList = contest.objects.all()
	Data = {
		'post' : post,
		'contestList' : contestList,
	}
	print(post)
	return render(req, "post_detail.html", Data)