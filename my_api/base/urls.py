from django.urls import path
from .views import RegisterAPIView, UsersApiView


urlpatterns = [
    path('register', RegisterAPIView.as_view()),
    path('all_users', UsersApiView.as_view())
]