from django import forms
from .models import Blog

class BlogPost(forms.ModelForm): #모델 기반의 form
    class Meta:
        model = Blog
        fields = ['title','body']

class BlogPost2(forms.Form): # 임의의 form (입력공간)
    email = forms.EmailField()
    files = forms.FileField()
    url = forms.URLField()
    words = forms.CharField(max_length = 200)
    max_number = forms.ChoiceField(choices = [('1','one'), ('2','two'), ('3', 'three')])


class PostForm(forms.Form):
    title = forms.CharField()
    content = forms.CharField(widget = forms.Textarea)

    def save(self, commit = True):
        post = Post(**self.cleaned_data)
        if commit:
            post.save()
            return post