from django.db import models


class Quiz(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    questions = models.ManyToManyField('Question', related_name='quizzes')

    def __str__(self):
        return self.title

class Question(models.Model):
    question_text = models.TextField()
    model_answer = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question_text

class QuizResponse(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.quiz.title}"
    
class QuestionResponse(models.Model):
    quiz_response = models.ForeignKey(QuizResponse, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    response = models.TextField(blank=True)
    grade = models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4')], null=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.quiz.title} - {self.question.question_text} - {self.response}"