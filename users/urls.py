from django.urls import path

from .views import RegisterCustomer, RegisterAdmin, LoginAdmin, LoginCustomer, AuthenticateUser, Logout, customer_list, customer_details, admin_list, admin_details

urlpatterns = [
    path('register-admin/', RegisterAdmin.as_view()),
    path('register-customer/', RegisterCustomer.as_view()),

    path('login-admin/', LoginAdmin.as_view()),
    path('login-customer/', LoginCustomer.as_view()),

    path('logout/', Logout.as_view()),
    path('authenticate/', AuthenticateUser.as_view()),
    path('customers/', customer_list),
    path('customers/<int:id>', customer_details),
    path('admins/', admin_list),
    path('admins/<int:id>', admin_details),
]
