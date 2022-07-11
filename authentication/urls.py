from django.urls import path
from .views import GetUserList, LoginView, RegisterView, UserProfileView

urlpatterns = [
    path('login/', LoginView.as_view()),
    path('register/', RegisterView.as_view()),
    path('profile/', UserProfileView.as_view()),
    path('admin/',GetUserList.as_view()),
]