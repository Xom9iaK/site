from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path
from django.urls import re_path
from fps import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('about/', views.about, name='about'),
    path('application/', views.application, name='application'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='fps/login.html'), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('handle-application/', views.handle_application, name='handle_application'),
    path('success/', views.success, name='success'),
    path('profile/', views.profile_view, name='profile'),
    path('add-review/<int:application_id>/', views.add_review, name='add_review'),
    path('edit-review/<int:review_id>/', views.edit_review, name='edit_review'),
    path('reorder/<int:application_id>/', views.reorder_service, name='reorder_service'),
    path('clear-applications/', views.clear_applications, name='clear_applications'),
    path('clear-notifications/', views.clear_notifications, name='clear_notifications'),
    path('vacancies/', views.vacancy_list, name='vacancies'),
    path('submit-job-application/<int:vacancy_id>/', views.submit_job_application, name='submit_job_application'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
