from django.urls import path
from . import views




urlpatterns = [
    path('reddit/post', views.RedditListCreate.as_view()),
    path('reddit/post/hot/new', views.RedditHotNew)
]

