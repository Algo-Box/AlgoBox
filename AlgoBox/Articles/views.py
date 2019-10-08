from django.shortcuts import render
from django.views import generic
from .models import Post
from .CListAPI import viewObject

def PostList(req):
	data = Post.objects.filter(status = 1).order_by('-created_on')
	contestList = viewObject()
	completeData = {
		'posts' : data,
		'contestList' : contestList,
	}
	return render(req, "index.html", completeData)
