from datetime import timedelta, datetime, date
from django.db import models
from django.utils.encoding import smart_text
from django.utils import timezone
from django.utils.text import slugify
from django.db.models.signals import post_save, pre_save
from .validators import validate_algo, validate_author_email
from django.utils.timesince import timesince
# Create your models here.

PUBLISH_CHOICES = (
    ('draft','Draft'),
    ('public','Public'),
    ('publish', 'Publish'),
    ('private','Private'),
)

class PostModelQuerySet(models.query.QuerySet):
    def active(self):
        return self.filter(title_icontains = True)

    def nuevo_title_items(self, value):
        return self.filter(title_icontains = value)

class PostModelManager(models.Manager):
    def get_queryset(self):
        return PostModelQuerySet(self.model, using = self._db)

    def all(self, *args, **kwargs):
        qs = super(PostModelManager,self).all(*args, **kwargs).filter(active = True)
        return (qs)

class Post(models.Model):
    id = models.BigAutoField(primary_key = True)
    active = models.BooleanField(default = True)
    title = models.CharField(max_length=250, default='NewPost',verbose_name='post title', unique = True,
    error_messages = {"unique":"Este titulo no es unico, intenta de nuevo con otro titulo"}, help_text = 'Debe de se un titulo unico')
    content = models.TextField(null=True, blank=True)
    publish = models.CharField(max_length=120, choices=PUBLISH_CHOICES, default="draft")
    slug = models.SlugField(null=True, blank=True)
    view_count = models.IntegerField(default=0)
    publish_date = models.DateField(auto_now=False, auto_now_add=False, default=timezone.now)
    author_email = models.EmailField(max_length = 240, validators=[validate_author_email, validate_algo], null=True, blank=True)
    update = models.DateTimeField (auto_now=True)
    timestamp = models.DateTimeField (auto_now_add=True)


    def __str__(self):
        return smart_text(self.content)

    def save (self, *args, **kwargs):
        print ("1ra Fase")
        if not self.slug:
            if self.title:
                self.slug = slugify (self.title)
        super (Post, self).save(*args, **kwargs)

    #Que es un decorador en python + 3 ejemplo

    @property
    def age(self):
        if self.publish=='publish':
            now =datetime.now()
            #now=datetime.combine(self.publish_date,datetime.now().min.time())
            publish_time =datetime.combine(
            self.publish_date,
            datetime.now().max.time()
            )
            try:
                difference= now - publish_time
            except:
                return "Desconocido"
                #difference='No nay publicación'
            if difference <= timedelta(minutes=1):
                return 'Ahora'
            return '{time} ago'.format(time=timesince(publish_time).split(', ')[0])
        return "No publicado"

def post_model_post_save_receiver(sender, instance, created, *args, **kwargs):
    print ("2da Fase")
    if not instance.slug and instance.title:
        instance.slug = slugify(instance.title)
        instance.save()

def post_model_pre_save_receiver(sender, instance, *args, **kwargs):
    print("1.5 ")
    if not instance.slug and instance.title:
        instance.slug=slugify(instance.title)
        instance.save()


post_save.connect(post_model_post_save_receiver, sender = Post)
pre_save.connect(post_model_pre_save_receiver, sender = Post)
