from django.contrib import admin
from django.urls import path, include

from .views import Welcome

from django.views.static import serve
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', Welcome, name='welcome'),
    path('api/auth/', include('users.urls')),
    path('api/store/',  include('store.urls')),
    path('admin/', admin.site.urls),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
