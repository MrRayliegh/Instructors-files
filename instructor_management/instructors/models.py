from django.db import models


class Instructor(models.Model):
    EMPLOYMENT_TYPE_CHOICES = [
        ('Regular', 'Regular'),
        ('COS', 'COS'),
    ]
    
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    employment_type = models.CharField(max_length=10, choices=EMPLOYMENT_TYPE_CHOICES)
    
    def __str__(self):
        return f"{self.last_name}, {self.first_name}"


class Instructor(models.Model):
    first_name = models.CharField(max_length=100, blank=False)  # First name is required
    last_name = models.CharField(max_length=100, blank=False)   # Last name is required
    email = models.EmailField(blank=True, null=True)            # Email can be optional
    phone = models.CharField(max_length=15, blank=True, null=True)  # Phone can be optional
    employment_type = models.CharField(
        max_length=10,
        choices=[('REGULAR', 'Regular'), ('COS', 'Contract of Service')],
        blank=False,  # Employment type is required
        null=False
    )
    bio = models.TextField(blank=True, null=True)  # Bio is optional

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    
    