from django.contrib import admin
from django.urls import path, include

from .views import dashboard
from store import views

from django.views.static import serve
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', dashboard, name='dashboard'),
    path('api/',  include('store.urls')),
    path('user/', include('users.urls')),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
