from django.shortcuts import render
from django.views import View  
from .models import user_blog


def insert_blog(request):
    if request.method == "POST":

        blog_heading = request.POST.get('blogHeading')
        blog_content = request.POST.get('content')

        # print(blog_heading, blog_content)  

        if blog_heading and blog_content:
            user_blog.objects.create(
                blog_heading=blog_heading,
                blog_content=blog_content
            )

            blogs = user_blog.objects.all()

            return render(request, 'blog.html', {'blogs': blogs})
        
