from django.urls import path

from .views import ListCreateBookAPIView

urlpatterns=[
    path("",ListCreateBookAPIView.as_view(),name='list-create-book'),
    ]
