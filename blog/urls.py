from django.urls import path
from . import views

urlpatterns =[
    path('blog', views.modelForm,),
    path('serializer/', views.serializer,)
]