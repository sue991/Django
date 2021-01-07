from django.shortcuts import render, get_object_or_404,redirect # import 필요!
from .models import Blog
from django.utils import timezone
from django.core.paginator import Paginator
from .form import BlogPost

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

def blogpost(request):
    if request.method == "POST":
        form = BlogPost(request.POST)

        if form.is_valid():
            post = form.save(commit = False) ### Blog 객체는 pub_date도 필요하다. 따라서 지금까지 작성한 form이 담긴 객체만 리턴하고 저장은 나중에 한다.
            post.pub_update = timezone.now() #현재 시간을 저장함
            post.save()
            return redirect('home')
    else:
        form = BlogPost()
        return render(request, 'new.html', {'form':form})
