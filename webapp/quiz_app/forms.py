# -*- coding: utf-8 -*-
from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions

from .models import *


class QuizForm(forms.ModelForm):

    helper = FormHelper()
    helper.add_input(Submit('submit', 'Create Quiz'))

    class Meta:
        model = Quiz
        fields = ['title', 'description']


class QuestionForm(forms.ModelForm):

    helper = FormHelper()

    helper.layout = Layout(
        Field('question_text', css_class='input-sm', rows='2'),
        Field('model_answer', css_class='input-xlarge', rows='5'),
        Submit('submit', 'Add Question'),
        Submit('finish', 'Finish Creating Quiz')
    )
    class Meta:
        model = Question
        fields = ['question_text', 'model_answer']


class ResponseForm(forms.ModelForm):

    helper = FormHelper()
    helper.layout = Layout(
        Field('question', readonly=True),
        Field('response', css_class='input-sm'),
        Submit('submit', 'Submit Response')
    )

    class Meta:
        model = QuestionResponse
        fields = ['question', 'response']
        widgets = {
            'question': forms.TextInput(attrs={'readonly': 'readonly'}),
        }