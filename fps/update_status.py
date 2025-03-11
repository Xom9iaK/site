from django.core.management.base import BaseCommand
from fps.models import Application
from django.utils import timezone
from datetime import timedelta

class Command(BaseCommand):
    help = 'Updates application statuses based on time'

    def handle(self, *args, **kwargs):
        # Update from 'processing' to 'assigned'
        processing_apps = Application.objects.filter(
            status='processing',
            created_at__lte=timezone.now() - timedelta(seconds=30)
        )
        processing_apps.update(status='assigned')

        # Update from 'assigned' to 'completed'
        assigned_apps = Application.objects.filter(
            status='assigned',
            updated_at__lte=timezone.now() - timedelta(seconds=30)
        )
        assigned_apps.update(status='completed')
