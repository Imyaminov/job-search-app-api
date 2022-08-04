from django.shortcuts import render
from rest_framework import generics, filters
from rest_framework.decorators import api_view

from .serializers import PostSerializers, StatusSerializers
from .models import Post, Status, Statistic
from .filters import PostFilter
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.

class PostApiView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializers

    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['job_position']#, 'min_price', 'max_price', 'location', 'job_status']
    ordering_fields = ['posted_date']#, 'max_price', 'min_price']
    # filterset_class = PostFilter

class StatisticApiView(generics.ListAPIView):
    queryset = Statistic.objects.all()
    serializer_class = StatusSerializers



