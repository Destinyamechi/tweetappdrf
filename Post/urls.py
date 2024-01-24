from django.urls import path
from .views import *

urlpatterns = [
    path('post/', allPostsView.as_view()),
    path('post/<str:slug>/',singlePostView.as_view()),
    path('create/', createPostView.as_view()),
    path('thread/<str:post_slug>/',createThreadView.as_view()),
    path('comment/<str:post_slug>/',createCommentView.as_view()),
    path('comment/<str:post_slug>/delete',deleteCommentView.as_view()),
    path('comment/<str:post_slug>/reply/<str:comment_slug>/',replyCommentView.as_view()),

    path('repost/<str:post_slug>',repostView.as_view()),
    path('quotetweet/<str:post_slug>',qouteTweetView.as_view()),



]