from django.urls import path
from . import views
urlpatterns = [
    path('', views.forum, name="forum"),
    path('post/<str:pk>/<str:title>', views.post, name="post" ),
]