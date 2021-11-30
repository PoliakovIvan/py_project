from django.contrib import admin
from django.urls import path, include
from blog.views import IndexView, BlogView, ItemView
app_name='blocg'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('blog/', BlogView.as_view(), name='blog'),
    path('item/<int:id>/',ItemView.as_view() , name='item'),

]