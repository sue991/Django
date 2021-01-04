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
        
  



---
참고 : https://egg-money.tistory.com/80?category=811218
