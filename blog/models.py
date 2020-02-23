from django.db import models
from django.utils import timezone as tz
from django.contrib.auth.models import User
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=100)
    date_posted = models.DateTimeField(default=tz.now)
    #as posts are unique to a author we use Foreign Keys
    author = models.ForeignKey(User, on_delete= models.CASCADE) 