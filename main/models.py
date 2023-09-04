from django.db import models
from slugify import slugify
from django.urls import reverse
#pip install python-slugify
import uuid
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
# Create your models here.

class BlogCreate (models.Model):
    author = models.ForeignKey(User, on_delete= models.SET_NULL, null = True ,related_name='author')
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=20)
    image_cover = models.ImageField(upload_to= 'images/')
    video = models.FileField(blank=True, null=True, upload_to= 'files/')
    audio = models.FileField(blank=True, null=True, upload_to= 'files/',)
    text = RichTextUploadingField(blank=True, null=True)
    description = models.CharField(max_length=200, default='This is a blog', null=True, blank=True)
    liked = models.ManyToManyField(User, default=None, blank=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    slug = models.UUIDField(default=uuid.uuid4, editable=False)

    def __str__(self):
        return self.title

    # @ property
    # def slug (self):
    #     return (slugify(self.title))
        # change something here

    @property
    def num_likes (self):
        return self.liked.all().count()

    def get_absolute_url(self):
        return reverse('updateblog', kwargs={'pk': self.id, 'slug': self.slug})

LIKE_CHOICES = (
    ('Like', 'Like'),
    ('Unlike', 'Unlike'),
)

class Like (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(BlogCreate, on_delete=models.CASCADE)
    value = models.CharField(choices= LIKE_CHOICES, default = 'Like', max_length = 10)
    date_added = models.DateTimeField(auto_now_add=True, blank=True, null=True )

    def __str__(self):
        return self.post.title

class Comment (models.Model):
    post = models.ForeignKey(BlogCreate, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return '%s - %s' % (self.post.title, self.user.username)
        


class Med (models.Model):
    favicon = models.ImageField()

class Genre (models.Model):
    genre1 = models.CharField(max_length=20)

    def __str__(self):
        return self.genre1