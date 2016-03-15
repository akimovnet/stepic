# -*- coding: utf-8 -*-

# form description

# AskForm - форма добавления вопроса
# title - поле заголовка
# text - поле текста вопроса

# AnswerForm - форма добавления ответа
# text - поле текста ответа
# question - поле для связи с вопросом

from django import forms
from django.contrib.auth.models import User
from qa.models import Question, Answer

class AskForm(forms.Form):

    title = forms.CharField()
    text = forms.CharField(widget=forms.Textarea)

    def save(self):
        self.cleaned_data['author_id'] = self._user_id
        return Question.objects.create(**self.cleaned_data)

class AnswerForm(forms.Form):

    text = forms.CharField(widget=forms.Textarea)
    question = forms.ModelChoiceField(queryset=Question.objects.all())

    def save(self):
        self.cleaned_data['author_id'] = self._user_id
        return Answer.objects.create(**self.cleaned_data)

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    def save(self):
        try:
            user = User.objects.get(username=self.cleaned_data['username'])
        except User.DoesNotExist:
            return None
        if user.password != self.cleaned_data['password']:
            return None
        return user

class SignupForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    def save(self):
        return User.objects.create(**self.cleaned_data)
