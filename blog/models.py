from django.db import models

# Create your models here.
class user_blog (models.Model):
    blog_heading = models.CharField(max_length=255)
    blog_content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)