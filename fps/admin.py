from django.contrib import admin
from fps.models import Application
from .models import UserProfile, Application, Review, Notification
from .models import Vacancy


admin.site.register(UserProfile)
admin.site.register(Application)
admin.site.register(Review)
admin.site.register(Notification)
admin.site.register(Vacancy)
