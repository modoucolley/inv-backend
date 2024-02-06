from django.db.models.signals import post_save
from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from .models import CustomUser
from .models import UserActivity

@receiver(post_save, sender=CustomUser)
def log_user_registration(sender, instance, created, **kwargs):
    if created:
        print(f"User {instance.email} logged in.")
        # Add user registration activity
        UserActivity.objects.create(user=instance, activity_type='registration', details='User registered')


@receiver(user_logged_in)
def user_logged_in_handler(sender, request, user, **kwargs):
    # This function will be called whenever a user logs in
    # You can perform any actions you want here, such as logging or updating user data
    print(f"User {user.username} logged in.")
    UserActivity.objects.create(user=user, activity_type='login', details=f"User {user.username} logged in.")
