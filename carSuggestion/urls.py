
from django.contrib import admin
from django.urls import path, include

admin.site.site_header = "WisdomWheels Admin"
admin.site.site_title = "WisdomWheels Admin Portal"
admin.site.index_title = "Welcome to WisdomWheels"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
]
