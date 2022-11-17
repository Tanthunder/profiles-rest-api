from . views import HelloApiView
from django.urls import path , include


urlpatterns = [
    path('hello-view/',HelloApiView.as_view())
]
