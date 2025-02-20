# Generated by Django 5.0.7 on 2024-07-17 18:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz_app', '0006_rename_quizresponse_questionresponse'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='questionresponse',
            name='quiz',
        ),
        migrations.AlterField(
            model_name='questionresponse',
            name='response',
            field=models.TextField(blank=True),
        ),
        migrations.CreateModel(
            name='QuizResponse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz_app.quiz')),
            ],
        ),
        migrations.AddField(
            model_name='questionresponse',
            name='quiz_response',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='quiz_app.quizresponse'),
            preserve_default=False,
        ),
    ]
