# instructors/urls.py

from django.urls import path
from .views import instructor_list, instructor_search, instructor_details  # Import your views

urlpatterns = [
    path('', instructor_list, name='instructor_list'),  # This line makes instructors/ work
    path('filter/', instructor_search, name='instructor_search'),  # Search functionality
    path('details/', instructor_details, name='instructor_details'),  # Instructor details
]
