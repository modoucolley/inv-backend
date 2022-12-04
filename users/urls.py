from django.urls import path

from .views import login_page, logout_page, Register, Login, LoginAdmin, AuthenticateUser, Logout, customer_list, customer_details, admin_list, admin_details

urlpatterns = [
    path('register/', Register.as_view()),
    path('login/', Login.as_view()),
    path('admin/login/', LoginAdmin.as_view()),
    path('logout/', logout_page, name='logout'),
    path('logout/', Logout.as_view()),
    path('authenticate/', AuthenticateUser.as_view()),
    path('customers/', customer_list),
    path('customers/<int:id>', customer_details),
    path('admins/', admin_list),
    path('admins/<int:id>', admin_details),



]
