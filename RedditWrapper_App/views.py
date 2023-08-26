from django.http import JsonResponse
from .reddit_client import get_reddit_data
from django.shortcuts import render

# Create your views here.
def get_reddit_threads(request):
    subreddit_name = 'news'
    data = get_reddit_data(subreddit_name)
    return JsonResponse(data, safe=False)

def index(request):
    return render(request, 'index.html')