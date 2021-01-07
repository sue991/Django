from django.shortcuts import render, get_object_or_404,redirect # import 필요!
from .models import Blog
from django.utils import timezone
from django.core.paginator import Paginator

# Create your views here.

def home(request):
    blogs = Blog.objects
    
    blog_list = Blog.objects.all()

    paginator = Paginator(blog_list,3)

    page = request.GET.get('page') # request된 페이지가 뭔지 알아내기

    posts = paginator.get_page(page) # request된 페이지를 얻어온 뒤 return

    return render(request, 'home.html', {'blogs' : blogs, 'posts' : posts})
    
def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk = blog_id)
    ### get_object_or_404(class, condition)
    ### pk : primary key
    return render(request, 'detail.html', {'blog' : blog_detail})


def new(request):
    return render(request, 'new.html')

def create(request):
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return redirect('/blog/'+str(blog.id))