from django.urls import path
from . import views
from django.conf.urls import static
from django.conf import settings

urlpatterns = [
    path('api/', views.APICLASSVIEW.as_view(), name='post'),
    path('api/<pk>/', views.APICLASSDDetailVIEW.as_view(), name='post-detail'),
]
