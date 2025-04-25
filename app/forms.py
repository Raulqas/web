# app/forms.py

from django import forms
from .models import Comment
from .models import Blog



class FeedbackForm(forms.Form):
    name = forms.CharField(label='Ваше имя', max_length=100, min_length=2)
    email = forms.EmailField(label='Email', max_length=100, min_length=2)
    rating = forms.ChoiceField(
        label='Оценка сайта',
        choices=[
            (1, '1 - Плохо'),
            (2, '2 - Удовлетворительно'),
            (3, '3 - Хорошо'),
            (4, '4 - Отлично'),
            (5, '5 - Превосходно')
        ],
        widget=forms.RadioSelect
    )
    likes = forms.MultipleChoiceField(
        label='Что вам понравилось?',
        choices=[
            ('design', 'Дизайн'),
            ('content', 'Содержимое'),
            ('speed', 'Скорость'),
            ('navigation', 'Навигация')
        ],
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    suggestion = forms.CharField(
        label='Ваши пожелания',
        widget=forms.Textarea,
        required=False,
        max_length=500
    )
    subscribe = forms.BooleanField(
        label='Подписаться на рассылку',
        required=False
    )

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
        labels = {'text': "Комментарий"}

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title', 'description', 'content', 'image')
        labels = {
            'title': 'Заголовок',
            'description': 'Краткое содержание',
            'content': 'Полное содержание',
            'image': 'Изображение',
        }