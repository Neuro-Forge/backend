from django.shortcuts import render
from django.views import View  
from .models import user_blog
from .serializaers import blog_serializer
from django.http import JsonResponse
from rest_framework.decorators import api_view

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
        
@api_view(['GET','POST'])
def serializer(request):
    """in this function  we are going to do first get the data from the database and 
    then we serialize it and  the we return that in a JSON fromat to the user  """
    if request.method == 'GET':
         Blog = user_blog.objects.all()
         BlogSerializer = blog_serializer(Blog, many=True)
         return JsonResponse(BlogSerializer.data, safe= False)  
    
    if request.method == 'POST':
        
        serializer = blog_serializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
         