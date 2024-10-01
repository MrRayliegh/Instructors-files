# instructors/admin.py

from django import forms
from django.contrib import admin
from .models import Instructor

class InstructorForm(forms.ModelForm):
    class Meta:
        model = Instructor
        fields = '__all__'  # Include all fields in the form

    def clean(self):
        cleaned_data = super().clean()
        if not cleaned_data.get('first_name'):
            self.add_error('first_name', 'This field should not be empty.')  # Custom error message
        if not cleaned_data.get('last_name'):
            self.add_error('last_name', 'This field should not be empty.')  # Custom error message
        if not cleaned_data.get('employment_type'):
            self.add_error('employment_type', 'This field should not be empty.')  # Custom error message

class InstructorAdmin(admin.ModelAdmin):
    form = InstructorForm
    list_display = ('first_name', 'last_name', 'email', 'phone', 'employment_type')
    search_fields = ('first_name', 'last_name', 'email')
    
    class Media:
        css = {
            'all': ('instructors/admin.css',)  # Link to your custom CSS
        }

# Customizing the admin site title
admin.site.site_header = 'CTU Dumanjug Extension Campus'  # Header title
admin.site.site_title = 'CTU Admin Panel'            # Browser tab title
admin.site.index_title = 'Welcome to CTU''s Admin Panel'  # Index page title

admin.site.register(Instructor, InstructorAdmin)
