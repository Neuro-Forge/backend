from rest_framework import serializers
from .models import user_blog

class blog_serializer(serializers.ModelSerializer):   
    class Meta:
        model = user_blog
        fields = "__all__"
