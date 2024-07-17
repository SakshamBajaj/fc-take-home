from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

from .models import *
from .forms import *


# index provides a list of all quizzes
def index(request):
    template_name = 'quiz_app/index.html'
    context = {
        'quizzes': Quiz.objects.all()
    }

    return render(request, template_name, context)




def create_quiz(request):

    def get_success_url(quiz):
        return f'/quiz_app/quiz/{quiz.id}/create_question'

    template_name = 'quiz_app/create_view.html'
    context = {
        'header': "Create Quiz"
    }

    form = QuizForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect(get_success_url(form.instance))
    context['form'] = form

    return render(request, template_name, context)

def create_question(request, quiz_id):
    template_name = 'quiz_app/create_view.html'
    quiz = get_object_or_404(Quiz, id=quiz_id)
    success_url = f'/quiz_app/quiz/{quiz_id}/create_question'
    finished_url = '/quiz_app/'
    context = {
        'header': f"Add Question for {quiz.title}"
    }

    form = QuestionForm(request.POST or None)

    if form.is_valid():
        form.save()
        quiz.questions.add(form.instance)
        if 'finish' in request.POST: # TODO: fix this bad hack
            return redirect(finished_url)
        return redirect(success_url)
    context['form'] = form

    return render(request, template_name, context)