# -*- coding: utf-8 -*-

# form description

# AskForm - форма добавления вопроса
# title - поле заголовка
# text - поле текста вопроса

# AnswerForm - форма добавления ответа
# text - поле текста ответа
# question - поле для связи с вопросом

from django import forms
from qa.models import Question, Answer

class AskForm(forms.Form):

    title = forms.CharField()
    text = forms.CharField(widget=forms.Textarea)

    def save(self):
        return Question.objects.create(**self.cleaned_data)

class AnswerForm(forms.Form):

    text = forms.CharField(widget=forms.Textarea)
    question = forms.ModelChoiceField(queryset=Question.objects.all())

    def save(self):
        return Answer.objects.create(**self.cleaned_data)
