from django.db import models
from django.utils.encoding import smart_text
from django.utils import timezone

from .validators import validate_algo, validate_author_email
# Create your models here.

PUBLISH_CHOICES = (
    ('draft','Draft'),
    ('public','Public'),
    ('private','Private'),
)

class Post(models.Model):
    id = models.BigAutoField(primary_key = True)
    active = models.BooleanField(default = True)
    title = models.CharField(max_length=250, default='NewPost',verbose_name='post title')
    content = models.TextField(null=True, blank=True)
    publish = models.CharField(max_length=120, choices=PUBLISH_CHOICES, default="draft")
    view_count = models.IntegerField(default=0)
    publish_date = models.DateField(auto_now=False, auto_now_add=False, default=timezone.now)
    author_email = models.EmailField(max_length = 240, validators=[validate_author_email, validate_algo], null=True, blank=True)

    def __str__(self):
        return smart_text(self.content)
    pass
