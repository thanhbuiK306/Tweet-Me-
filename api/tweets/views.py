from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.utils.http import url_has_allowed_host_and_scheme
from django.conf import settings

from .models import Tweet
from random import randrange
from .forms import TweetCreateForm
# Create your views here.

ALLOWED_HOSTS = settings.ALLOWED_HOSTS
def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

def homepage(request, *args, **kwargs):
    return render(request, 'pages/home.html', context = {}, status= 200)

def TweetList(request, *args, **kwargs):
    qs = Tweet.objects.all()
    tweet_list = [x.serialize() for x in qs]
    data ={
        "response": tweet_list
    }
    
    return JsonResponse(data)

def TweetCreateView(request, *args, **kwargs):
    form = TweetCreateForm(request.POST or None)
    next_url = request.POST.get('next') or None
    if form.is_valid():
        tweetObj = form.save(commit=False)
        tweetObj.save()
        if is_ajax(request):
            return JsonResponse(tweetObj.serialize(), status = 201) #201 == created - item
        if next_url !=None and url_has_allowed_host_and_scheme(next_url, ALLOWED_HOSTS):
            return redirect(next_url)
        form = TweetCreateForm()
    if form.errors:
        if is_ajax(request):
            return JsonResponse(form.errors, status = 400)
        
    return render(request, 'components/form.html', context ={"form": form})