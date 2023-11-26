from django.db import models
from random import randrange
# Create your models here.
class Tweet(models.Model):
    content = models.TextField()
    file = models.FileField(upload_to='local/', max_length=200)
    class Meta:
        ordering = ['-id']
    def serialize(self):
        return {
            "id":self.id,
            "content":self.content,
            "likes":randrange(10000)
        }