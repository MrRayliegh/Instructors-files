# instructors/views.py
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from .models import Instructor
from django.db.models import Q  

def instructor_list(request):
    query = request.GET.get('q', '')
    filter_type = request.GET.get('filter', 'ALL')  # Default to 'ALL'

    instructors = Instructor.objects.all()  # Start with all instructors

    # Apply filtering based on the filter type
    if filter_type != 'ALL':
        instructors = instructors.filter(employment_type=filter_type)

    # Apply searching based on the query
    if query:
        instructors = instructors.filter(
            Q(first_name__icontains=query) | 
            Q(last_name__icontains=query) | 
            Q(email__icontains=query)
        )

    return render(request, 'instructors/instructor_list.html', {
        'instructors': instructors,
        'filter': filter_type,
        'query': query,  # Pass the query to the template context
    })

def instructor_search(request):
    query = request.GET.get('q', '')
    filter_type = request.GET.get('filter', 'ALL')

    # Perform filtering based on the query and filter type
    if filter_type == 'REGULAR':
        results = Instructor.objects.filter(first_name__icontains=query, employment_type='REGULAR')
    elif filter_type == 'COS':
        results = Instructor.objects.filter(first_name__icontains=query, employment_type='COS')
    else:  # 'ALL' or no filter selected
        results = Instructor.objects.filter(first_name__icontains=query)

    # Prepare the results for JSON response
    suggestions = [{'id': instructor.id, 'name': f"{instructor.first_name} {instructor.last_name}"} for instructor in results]
    
    return JsonResponse({'results': suggestions})
def instructor_details(request):
    instructor_id = request.GET.get('id')
    try:
        instructor = Instructor.objects.get(id=instructor_id)
        data = {
            'html': f"<h3>{instructor.first_name} {instructor.last_name}</h3><p>Email: {instructor.email}</p><p>Phone: {instructor.phone}</p><p>Type: {instructor.employment_type}</p>"
        }
        return JsonResponse(data)
    except Instructor.DoesNotExist:
        return JsonResponse({'error': 'Instructor not found'}, status=404)

def filter_instructors(request):
    # Logic for filtering instructors can be added here
    return render(request, 'instructors/instructor_filter.html')
