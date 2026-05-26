from django.db import models
class Post(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    publish_date = models.DateField()
    author = models.CharField(max_length=100)

    def __str__(self):
        return self.title
# Create your models here.
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField()
    author = models.CharField(max_length=100)

    def __str__(self):
        return self.author