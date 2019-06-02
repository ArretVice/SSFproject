from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(auto_now_add=True)
    date_last_edited = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    class Meta:
        ordering = ['-date_posted']

    def __str__(self):
        return self.title

    def preview(self, preview_len=500):
        if len(self.content) > preview_len:
            return self.content[:preview_len] + '...'
        else:
            return self.content
