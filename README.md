# Django

## 210104
- 환경변수, django server, project 및 app 직접 만들어보기

- 환경변수 
`source web-env/bin/activate`

- 장고 서버 실행
`python3 manage.py runserver`

- testproject
  + helloworld // App1
  + testproject // Project
  + wordcount // App2
  
- helloword
  + `127.0.0.1:8000/hello`
  + hello world!

- wordcount
  + `127.0.0.1:8000`
  + 단어 수 세기
 
 
---
 
- secondprogect : blog 만들기

- admin, model.py를 이용한 DB 다루기

- secondproject
  + blog // App1
  + secondproject // Progect

- templates
  + home.html // Blog home 화면, 글 목록
  + detail.html // 각각 글 자세히
  + new.html // 글쓰기
  
- blog
  + `127.0.0.1:8000` // home.html
  + `127.0.0.1:8000/blog/{blog_id}` // detail.html
  + `http://127.0.0.1:8000/blog/new` // 새로운 글 작성 후 제출
  + create : 새로운 글 업로드 후 생성한 blog/{id} page로 redirect
 
- path converter, get_object_or_404,redirect 사용
        
  
## 210105
- static, media 응용
  + static : 미리 서버에 저장되어있는 파일
  + media : 웹 서비스 이용자들이 업로드하는 파일. url 통해 외부와 통신
  
- App 에 static 폴더 만들고 사용
- `python manage.py collectstatic` 통해 static 파일 모아주기. 
- `urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)` 사용해 URL로 사용자가 업로드한 media 파일에 접근.

---

- template 상속과 url 관리

- templates
  + Project폴더에 templates 생성.
  + 프로젝트 전반에 적용함
  + `'DIRS': ['secondproject/templates']` 추가
  + block contents , endblock 활용
```django
{% extends 'base.html' %}

{% block contents %}

{% endblock %}
```
  
- URL 관리
  + Project가 아닌 App에서 `url.py` 생성 후 url 관리
  + `from . import views` // app.urls.py
  + `from django.urls import include` // project.urls.py

##210106

- Sign Up, Login, Logout 기능 구현
- Django 에는 이미 기능이 있음

- HTTP method 'POST' 방식 사용
  + `{% csrf_token %}`  // 사이트간 요청 위조(Cross Site Request Forgery) 공격을 막기 위한 코드
  + `from django.contrib.auth.models import User` // signup, login을 위한 기능
  + `from django.contrib import auth` // signup, login을 위한 기능
 
```python3
user = User.objects.create_user(username = request.POST['username'], password = request.POST['password1'])
auth.login(request, user)
auth.logout(request)
```

##210107

- Pagination 사용
  + `from django.core.paginator import Paginator // blog.views.py`

- 밑으로만 계속 생성되는 글을 잘라서 여러 페이지로 보여주기

```python3

blog_list = Blog.objects.all()
paginator = Paginator(blog_list,3) # 한 페이지에 3개의 글
page = request.GET.get('page') # request된 페이지가 뭔지 알아내기
posts = paginator.get_page(page) # request된 페이지를 얻어온 뒤 return

```

- Faker
  + 많은 Data를 가진 환경 속에서 기능을 구현할 때 사용한다.
  + 임의의 데이터를 만드는것
  + `pip3 install faker`
  + `from faker import Faker // fake.py`

- Meta class
  + class들을 정의하기 위한 class
  + 상위 개념으로 클래스들을 묶어놓는 것
  
```python3
from django import forms 

class myForm(forms.ModelForm): 
  class Meta:
```

- Form.py
  + 모델을 기반으로 한 입력공간 : 장고에서 default 로 사용하는 model 틀을 가져다가 쓸 것이기 때문에 import 해줘야 한다.
    * `from django import forms.ModelForm`
  
  + 임의의 입력공간
    * `from django import forms.Form`

  + `form.save(commit=False)`
    * 지금까지 작성한 form이 담긴 객체만 리턴하고 저장은 나중에.
    
  + form을 사용하는 이유 : `views.py`에서 어떤 변수는 어떻게 받아서 넣어줘! 와 같은 작업을 할 필요 없이 자동으로 넣어준다는 장점이 있다.


---
참고 : https://egg-money.tistory.com/80?category=811218
