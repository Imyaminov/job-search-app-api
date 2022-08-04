from .serializers import PostSerializers, StatusSerializers
from .models import Post, Status
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework

class PostFilter(rest_framework.FilterSet):

     class Meta:
         model = Post
         fields = ['job_position', 'min_price', 'max_price', 'location', 'job_status']