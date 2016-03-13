# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('qa', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='added_at',
            field=models.DateField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='answer',
            name='author',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='answer',
            name='question',
            field=models.OneToOneField(null=True, to='qa.Question'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='question',
            name='author',
            field=models.ForeignKey(related_name='my_questions', to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='question',
            name='likes',
            field=models.ManyToManyField(related_name='favorite_questions', null=True, to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
