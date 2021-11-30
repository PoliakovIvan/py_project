from django.contrib import admin
from blog.models import Post, Page

@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    pass

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('author',)

    def save_models(self, request, obj, form, change):
        obj.author = request.user
        super(),save_model(request, obj, form, change)
