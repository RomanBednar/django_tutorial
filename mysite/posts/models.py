from django.db import models
from django.db import models
# Create your models here.

class Post(models.Model):
    post_text = models.CharField(max_length=50)
    date_published = models.DateTimeField('date published')

    def __str__(self):
        return self.post_text