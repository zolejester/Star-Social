#Groups URLS
#lesson 8
from django.urls import path
from . import views

app_name='groups' #This is used so that the url template tagging in the html works

urlpatterns = [
    path('', views.ListGroup.as_view(), name='all'),
    path('new/', views.CreateGroup.as_view(), name='create'),
    #path('posts/in/(?p<slug>[-\w]+)/',views.SingleGroup.as_view(), name='single')
    path('posts/in/<slug:slug>/',views.SingleGroup.as_view(), name='single'),
    path('join/in/<slug:slug>/',views.JoinGroup.as_view(), name='join'),
    path('leave/in/<slug:slug>/',views.LeaveGroup.as_view(), name='leave'),

]
