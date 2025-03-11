from django.utils import timezone
from .models import Application, Notification
from datetime import timedelta
from django.conf import settings
from django.utils.deprecation import MiddlewareMixin
class StatusUpdateMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        self.update_statuses()
        response = self.get_response(request)
        return response

    def update_statuses(self):
        # Processing to Assigned
        processing_apps = Application.objects.filter(
            status='processing',
            created_at__lte=timezone.now() - timedelta(seconds=30)
        )
        for app in processing_apps:
            app.status = 'assigned'
            app.save()
            Notification.objects.create(
                user=app.user,
                message=f'Статус вашей заявки №{app.id} изменен на "Назначен мастер"'
            )

        # Assigned to Completed
        assigned_apps = Application.objects.filter(
            status='assigned',
            updated_at__lte=timezone.now() - timedelta(seconds=30)
        )
        for app in assigned_apps:
            app.status = 'completed'
            app.save()
            Notification.objects.create(
                user=app.user,
                message=f'Статус вашей заявки №{app.id} изменен на "Выполнено"'
            )
            
class AdminSessionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Для пути /admin используем отдельное имя cookie
        if request.path.startswith('/admin'):
            settings.SESSION_COOKIE_NAME = 'admin_sessionid'
        else:
            settings.SESSION_COOKIE_NAME = 'user_sessionid'

        response = self.get_response(request)
        return response
