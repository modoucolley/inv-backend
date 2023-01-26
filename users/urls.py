from django.urls import path

from .views import RegisterUser, LoginUser, UserRetreiveUpdateDeleteView, BlacklistTokenUpdateView

urlpatterns = [
    path('register/', RegisterUser.as_view(), name='register_user'),
    path('login/', LoginUser.as_view(), name='login_user'),

    path('userdetails/<str:pk>/', UserRetreiveUpdateDeleteView.as_view(), name='detailupdatedeleteproducts'),

]