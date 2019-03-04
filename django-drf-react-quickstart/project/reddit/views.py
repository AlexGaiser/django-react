from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers

from reddit.models import RedditPostsHot
from reddit.serializers import RedditSerializer
from rest_framework import generics

# import cfg, schema, nlp_script, insert_pgdb, geddit
from reddit.collection_app import geddit
class RedditListCreate(generics.ListCreateAPIView):
    queryset = RedditPostsHot.objects.filter(karma__gte = 10000)[:10]
    serializer_class = RedditSerializer
    
def RedditHotNew(request):
 
    
    geddit.get_reddit_data(subreddit="all", sort="hot", limit=1000)

    qs = RedditPostsHot.objects.order_by('-collected_date')[:20]
    qs = list(qs.values())

    return JsonResponse({'data':qs}, safe = False)
    # JsonResponse(qs, safe = False)
