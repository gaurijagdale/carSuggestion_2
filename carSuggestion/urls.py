
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = "WisdomWheels Admin"
admin.site.site_title = "WisdomWheels Admin Portal"
admin.site.index_title = "Welcome to WisdomWheels"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
]

# Add URL patterns for serving media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
