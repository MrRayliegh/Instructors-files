# instructor_management/urls.py

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('instructors/', include('instructors.urls')),  # Include the instructors app URLs
]
