from django.contrib.auth import logout
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django import forms
from . import forms
from .forms import ApplicationForm, SimpleUserCreationForm
from .models import Application, Review, Notification, UserProfile
from .forms import UserProfileForm, ReviewForm
from .models import Notification
from .models import Vacancy
from .forms import JobApplicationForm
from django.contrib import messages

def home(request):
    return render(request, 'fps/home.html')

def about(request):
    return render(request, 'fps/home.html', {'scroll_to': 'about'})

def logout_view(request):
    logout(request)
    return redirect('login')
def register(request):
    if request.method == 'POST':
        form = SimpleUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SimpleUserCreationForm()
    return render(request, 'fps/register.html', {'form': form})

def handle_application(request):
    if request.user.is_authenticated:
        return redirect('application')
    return redirect('login')
def application(request):
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            application = form.save(commit=False)
            application.user = request.user
            application.save()
            
            # Create notification for new application
            Notification.objects.create(
                user=request.user,
                message=f'Ваша заявка №{application.id} успешно создана'
            )
            
            messages.success(request, 'Заявка успешно отправлена!')
            return redirect('success')
    else:
        form = ApplicationForm()
    return render(request, 'fps/application.html', {'form': form})

def success(request):
    return render(request, 'fps/success.html')

def login_view(request):
    # Add login logic here
    return render(request, 'fps/login.html')

def register_view(request):
    # Add registration logic here
    return render(request, 'fps/register.html')

@login_required
def profile_view(request):
    applications = Application.objects.filter(user=request.user).order_by('-created_at')
    notifications = Notification.objects.filter(user=request.user, is_read=False)
    
    try:
        profile = request.user.userprofile
    except UserProfile.DoesNotExist:
        profile = UserProfile.objects.create(user=request.user)
    
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserProfileForm(instance=profile)
    
    context = {
        'applications': applications,
        'notifications': notifications,
        'form': form,
    }
    return render(request, 'fps/profile.html', context)

@login_required
def add_review(request, application_id):
    if request.method == 'POST':
        application = get_object_or_404(Application, id=application_id, user=request.user)
        Review.objects.create(
            application=application,
            text=request.POST.get('text')
        )
        return redirect('profile')
    return redirect('profile')

@login_required
def edit_review(request, review_id):
    review = get_object_or_404(Review, id=review_id, application__user=request.user)
    if request.method == 'POST':
        review.text = request.POST.get('text')
        review.save()
    return redirect('profile')

@login_required
def reorder_service(request, application_id):
    old_application = get_object_or_404(Application, id=application_id)
    new_application = Application.objects.create(
        user=request.user,
        email=old_application.email,
        phone=old_application.phone,
        service=old_application.service
    )
    return redirect('profile')

@login_required
def clear_applications(request):
    if request.method == 'POST':
        Application.objects.filter(user=request.user).delete()
        messages.success(request, 'История заявок успешно очищена')
    return redirect('profile')

@login_required
def clear_notifications(request):
    if request.method == 'POST':
        Notification.objects.filter(user=request.user).delete()
        messages.success(request, 'История уведомлений очищена')
    return redirect('profile')

def vacancy_list(request):
    vacancies = Vacancy.objects.all().order_by('-created_at')
    form = JobApplicationForm()
    return render(request, 'fps/vacancies.html', {
        'vacancies': vacancies,
        'form': form
    })

@login_required
def submit_job_application(request, vacancy_id):
    if request.method == 'POST':
        vacancy = get_object_or_404(Vacancy, id=vacancy_id)
        form = JobApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            application = form.save(commit=False)
            application.vacancy = vacancy
            application.save()
            
            # Create notification for new job application
            Notification.objects.create(
                user=request.user,
                message=f'Ваш отклик на вакансию "{vacancy.title}" успешно отправлен'
            )
            
            messages.success(request, 'Ваш отклик успешно отправлен!')
            return redirect('vacancies')
        else:
            messages.error(request, 'Пожалуйста, проверьте правильность заполнения формы')
    
    return redirect('vacancies')

