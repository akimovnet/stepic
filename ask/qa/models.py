# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

#Question - вопрос
#title - заголовок вопроса
#text - полный текст вопроса
#added_at - дата добавления вопроса
#rating - рейтинг вопроса (число)
#author - автор вопроса
#likes - список пользователей, поставивших "лайк"
#
#Answer - ответ
#text - текст ответа
#added_at - дата добавления ответа
#question - вопрос, к которому относится ответ
#author - автор ответа

class Question(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateField(null=True)
    rating = models.IntegerField(null=True)
    author = models.ForeignKey(User, related_name='my_questions')
    likes = models.ManyToManyField(User, related_name='favorite_questions')

    def get_url(self):
        return reverse('qa:qa-question', kwargs={'id': self.pk})

class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateField()
    question = models.OneToOneField(Question)
    author = models.ForeignKey(User)
