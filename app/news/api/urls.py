from django.urls import path,include
from news.api.views import *

urlpatterns = [
    path('journalists/',JournalistListCreateAPIView.as_view(),name='journalists-list'),
    path('news/',NewsListCreateAPIView.as_view(),name='news-list'),
    path('news/<int:pk>/',NewsDetailAPIView.as_view(),name='news'),
]