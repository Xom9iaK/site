from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=15, blank=True)
    email = models.EmailField(blank=True)
    
class Application(models.Model):
    STATUS_CHOICES = [
        ('processing', 'В обработке'),
        ('assigned', 'Назначен мастер'),
        ('completed', 'Выполнено'),
    ]
    
    SERVICE_CHOICES = [
        ('repair', 'Ремонт оборудования'),
        ('check', 'Проверка оборудования'),
        ('replace', 'Замена оборудования'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    service = models.CharField(max_length=10, choices=SERVICE_CHOICES)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='processing')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Review(models.Model):
    application = models.ForeignKey(Application, on_delete=models.CASCADE, related_name='reviews')
    text = models.TextField(verbose_name='Текст отзыва')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Review for {self.application}'

class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']
        
class Vacancy(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название вакансии')
    short_description = models.TextField(verbose_name='Краткое описание')
    responsibilities = models.TextField(verbose_name='Обязанности')
    requirements = models.TextField(verbose_name='Требования')
    conditions = models.TextField(verbose_name='Условия работы')
    location = models.CharField(max_length=200, verbose_name='Местоположение')
    contact_info = models.TextField(verbose_name='Контактная информация')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'

    def __str__(self):
        return self.title

class Vacancy(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название вакансии')
    description = models.TextField(verbose_name='Краткое описание обязанностей', null=True, blank=True)
    requirements = models.TextField(verbose_name='Требования к кандидату', null=True, blank=True)
    conditions = models.TextField(verbose_name='Условия работы', null=True, blank=True)
    salary = models.CharField(max_length=100, verbose_name='Зарплата', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'

    def __str__(self):
        return self.title
    
class JobApplication(models.Model):
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, verbose_name='Имя')
    phone = models.CharField(max_length=20, verbose_name='Телефон')
    email = models.EmailField(verbose_name='Email')
    resume = models.FileField(upload_to='resumes/', verbose_name='Резюме')
    cover_letter = models.TextField(blank=True, null=True, verbose_name='Сопроводительное письмо')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Application from {self.name} for {self.vacancy.title}"