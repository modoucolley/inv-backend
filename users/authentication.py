from django.contrib.auth.backends import BaseBackend
from .models import CustomUser

class CustomUserBackend(BaseBackend):
    def authenticate(self, request, email=None, password=None, phone_number=None, pin=None):
        if email and password:
            try:
                user = CustomUser.objects.get(email=email, is_active = True)
                if user.check_password(password):
                    return user
            except CustomUser.DoesNotExist:
                return None
        elif phone_number and pin:
            try:
                user = CustomUser.objects.get(phone_number=phone_number, is_active = True)
                if user.check_pin(pin):
                    return user
            except CustomUser.DoesNotExist:
                return None
        return None

    def get_user(self, user_id):
        try:
            return CustomUser.objects.get(pk=user_id), 
        except CustomUser.DoesNotExist:
            return None
