from django.urls import path
from .views import homepage, TweetList, TweetCreateView

urlpatterns = [
    path('', homepage),
    path('tweets/', TweetList),
    path('create-tweet/', TweetCreateView)
]
