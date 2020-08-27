"""DEfines URL patterns for django_practical."""

from django.urls import path
from . import views

app_name = 'django_practical'
urlpatterns = [
    # Homepage
    path('', views.index, name='index'), 
    # Page that shows all topics
    path('topics/', views.topics, name='topics'), 
    # Detail page for a topic
    path('topics/<int:topic_id>/', views.topic, name='topic'),
] 