from django.shortcuts import render, get_object_or_404
from django.views import View
from blog.models import Post, Page

class IndexView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'index.html',{
            'page': get_object_or_404(Page, unique_name='index')
    })

class BlogView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'blog.html', {
            'page': get_object_or_404(Page, unique_name='blog'),
            'posts': Post.objects.all(),

        })

class ItemView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'item.html', {
            'posts': get_object_or_404(Post, id=kwargs['id']),
        })
