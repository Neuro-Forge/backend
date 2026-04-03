from django.db import models

# Create your models here.
class Quote(models.Model):
    quote = models.CharField(max_length=255)
    submitted_at = models.DateTimeField(auto_now_add=True)
    