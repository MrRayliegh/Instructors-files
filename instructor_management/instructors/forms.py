
from django import forms
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

class InstructorSearchForm(forms.Form):
    query = forms.CharField(label='Search', max_length=100, required=False)

    def clean_query(self):
        query = self.cleaned_data.get('query')
        if not query:
            raise forms.ValidationError("This field cannot be empty.")
        return query
