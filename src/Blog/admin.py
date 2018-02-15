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
        'get_age'
        #'new_content'
    ]
    readonly_fields = ['update', 'timestamp', 'get_age'] #'new_content'

    def new_content(self, obj, *args, **kwargs):
        return str(obj.title)

    def get_age(self, obj, *args, **kwargs):
        return str(obj.age)

    class Meta:
        model = Post


admin.site.register(Post, PostModelAdmin)
