from django.shortcuts import render , redirect
from django.shortcuts import render_to_response
from .models import Blog
from django.http import Http404
from django.http import HttpResponseRedirect
from forms import NewBlog
		
def index(request):
	flag = True
	if not request.user.is_authenticated():
		flag = False

	latest_blog_list = Blog.objects.filter(show=True)
	# print flag
	context = {'latest_blog_list': latest_blog_list,'flag': flag}
	return render(request,'blogs/index.html',context)

def detail(request, blog_id):
	curr_user = request.user
	try:
		blog = Blog.objects.get(pk=blog_id)
	except Blog.DoesNotExits:
		raise Http404("Blog does not exits")

	return render(request,'blogs/detail.html',{'blog':blog,'curr_user':curr_user})

def add_blog(request):
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404
	if not request.user.is_authenticated():
		raise Http404

	title = "Add New Blog"
	form = NewBlog(request.POST or None)
	if form.is_valid():
		blog = form.save(commit=False)
		blog.user = request.user
		body = blog.body
		blog.body = body.encode('ascii', 'ignore')
		blog.save()
		return redirect('/')
	return render(request,'blogs/blog_form.html',{"form":form, "title":title})

def profile(request):
	blogs_list = Blog.objects.all()
	my_list = []
	for i in blogs_list:
		if(i.user==request.user):
			my_list.append(i)
	curr_user = request.user
	return render(request,'blogs/my_page.html',{'my_list':my_list,'curr_user':curr_user})
def edit(request,blog_id):
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404
	if not request.user.is_authenticated():
		raise Http404
	my_record = Blog.objects.get(id=blog_id)
	# print my_record.user,request.user 

	form = NewBlog( request.POST or None,instance=my_record)
	# form = NewBlog(request.POST, instance=my_record)
	title = "update blog"
	if form.is_valid():
		blog = form.save(commit=False)
		blog.user = request.user
		blog.save()
		return redirect('/')
	return render(request,'blogs/blog_form.html',{"form":form, "title":title})