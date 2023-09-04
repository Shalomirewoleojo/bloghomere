from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dob = models.DateField()
    image = models.ImageField(blank=True, null=True, upload_to='images/users/')
    # author = models.BooleanField(blank=True, null=True)

    def __str__(self):
        return self.user.username

class Followers(models.Model):
    followed = models.ForeignKey(User, on_delete=models.CASCADE)
    follower = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return '%s - %s' % (self.followed, self.follower)