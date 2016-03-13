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

    def __init__(self, question, *args, **kwargs):
        self._question = question
        super(AnswerForm, self).__init__(*args, **kwargs)

    text = forms.CharField(widget=forms.Textarea)
    # question = forms.ModelChoiceField(queryset=Question.objects.all())

    def save(self):
        self.cleaned_data['question'] = self._question
        return Answer.objects.create(**self.cleaned_data)
