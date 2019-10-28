from django.shortcuts import render
from .models import Post
from APIServer.models import contest
from . import forms
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
def create_article(req):
	if req.method == 'POST':
		form = forms.CreateArticle(req.POST, req.FILES)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.author = req.user
			instance.save()
			return render(req, "pstd.html")
	else:
		form = forms.CreateArticle()
	return render(req, "create_article.html", {'form': form})