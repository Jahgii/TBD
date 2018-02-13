from django.contrib import admin

# Register your models here.
from .models import Post

class PostModelAdmin(admin.ModelAdmin):
    fields = [
        'title',
        'slug',
        'content',
        'publish',
        'publish_date',
        'active',
        'update',
        'timestamp',
        'new_content'
    ]
    readonly_fields = ['update', 'timestamp', 'new_content']

    def new_content(self, obj, *args, **kwargs):
        return str(obj.title)

    class Meta:
        model = Post


admin.site.register(Post, PostModelAdmin)
