# Generated by Django 5.0.7 on 2024-07-17 17:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz_app', '0005_quizresponse'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='QuizResponse',
            new_name='QuestionResponse',
        ),
    ]
