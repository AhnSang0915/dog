from django.urls import path

from puppy.views import OwnersView, DogsView

urlpatterns = [
    path('/owners',OwnersView.as_view()),
    path('/dogs',DogsView.as_view())
]
