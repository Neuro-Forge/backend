from django.urls import path
from . import views

urlpatterns =[
    path('blog', views.insert_blog,),
    path('serializer/', views.serializer,)
]