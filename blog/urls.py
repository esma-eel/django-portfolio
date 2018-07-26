
from django.urls import path

from . import views
# from django.urls import include, path

urlpatterns = [
    path('', views.allblogs, name="allblogs"),
    path('<int:blog_id>/', views.detail, name='detail'),
]
