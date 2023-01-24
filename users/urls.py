from django.urls import path

from .views import RegisterUser, LoginUser, BlacklistTokenUpdateView

urlpatterns = [
    path('register/', RegisterUser.as_view(), name='register_user'),
    path('login/', LoginUser.as_view(), name='login_user'),
]