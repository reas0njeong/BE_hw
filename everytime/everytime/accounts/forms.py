from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

class SignUpForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ['university', 'email', 'nickname', 'username']
        labels = {
            'university': '학교',
            'email': '이메일',
            'nickname': '닉네임',
            'username': '사용자 이름',
        }