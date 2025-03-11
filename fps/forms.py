from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile, Review, Application
from .models import JobApplication



class SimpleUserCreationForm(UserCreationForm):
    username = forms.CharField(
        max_length=150,
        help_text='',
        label='Имя пользователя'
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(),
        help_text='',
        label='Пароль'
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(),
        help_text='',
        label='Подтверждение пароля'
    )

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['email', 'phone', 'service']


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'email', 'phone']
        labels = {
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'email': 'Email',
            'phone': 'Телефон'
        }

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={
                'rows': 3,
                'placeholder': 'Напишите ваш отзыв'
            })
        }
        
class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = ['name', 'phone', 'email', 'resume', 'cover_letter']
        widgets = {
            'cover_letter': forms.Textarea(attrs={'placeholder': 'Необязательно'}),
        }