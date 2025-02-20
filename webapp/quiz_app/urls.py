from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("create/", views.create_quiz, name="create_quiz"),
    path("quiz/<int:quiz_id>/create_question", views.create_question, name="create_question"),
    path("response/<int:response_id>/question/<int:question_id>/create_response", views.create_response, name="create_response"),
]