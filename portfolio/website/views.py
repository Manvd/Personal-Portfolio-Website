from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from .models import contact as ContactModel


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def skills(request):
    return render(request, 'skills.html')


def projects(request):
    return render(request, 'projects.html')


@require_http_methods(["GET", "POST"])
def contacts(request):
    if request.method == 'POST':
        try:
            # Pull data from POST
            first_name   = request.POST.get('first_name', '').strip()
            last_name    = request.POST.get('last_name', '').strip()
            email        = request.POST.get('email', '').strip()
            company      = request.POST.get('company', '').strip()
            project_type = request.POST.get('Project_type', '').strip()
            budget       = request.POST.get('budget', '').strip()
            message      = request.POST.get('message', '').strip()

            # Basic server-side validation
            errors = []
            if not first_name:
                errors.append('First name is required.')
            if not email:
                errors.append('Email address is required.')
            if not message:
                errors.append('Message is required.')

            if errors:
                return JsonResponse({'success': False, 'error': ' '.join(errors)}, status=400)

            # Save to database
            ContactModel.objects.create(
                first_name   = first_name,
                last_name    = last_name,
                email        = email,
                company      = company,
                Project_type = project_type,
                budget       = budget,
                message      = message,
            )

            return JsonResponse({'success': True})

        except Exception as e:
            return JsonResponse({'success': False, 'error': 'Server error. Please try again.'}, status=500)

    # GET — just render the page
    return render(request, 'contacts.html')
