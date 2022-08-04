from . import views
from django.urls import path

urlpatterns = [
    path('post/', views.PostApiView.as_view()),
    path('statistic', views.StatisticApiView.as_view()),
]