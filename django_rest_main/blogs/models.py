from django.db import models

# Create your models here.

class Blogs(models.Model):
    blog_title = models.CharField(max_length=50)
    blog_body = models.TextField()

    def __str__(self):
        return self.blog_title
    
class Comments(models.Model):
    blog = models.ForeignKey(Blogs, on_delete=models.CASCADE, related_name='comments')
    comment = models.TextField()

    def __str__(self):
        return self.comment
    