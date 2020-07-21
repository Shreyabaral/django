from django.urls import path
from . import views
app_name = 'Blog'
urlpatterns= [
   path('', views.index.as_view(template_name="Blog/blogpost_list.html"), name='blogpost'),
    path('<slug:pk>/authors/', views.authors.as_view(), name='authors'),
 ]
