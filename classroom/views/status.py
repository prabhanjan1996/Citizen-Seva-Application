from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.db.models import Avg, Count
from django.forms import inlineformset_factory
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)

from ..decorators import teacher_required
from ..forms import BaseAnswerInlineFormSet, QuestionForm, TeacherSignUpForm, StatusForms
from ..models import Answer, Question, Quiz, User, Complaint
from reportlab.pdfgen import canvas
from django.http import HttpResponseRedirect, HttpResponse
from io import BytesIO
from reportlab.lib.units import inch


def rev(request):
    return HttpResponse('<br><br>'
                        
                        '<center><h1>Status updated successfully '
                        '<br><br>'
                        '<a href = "/" >back</a></h1></center>')


class QuizUpdateView2(UpdateView):
    model = Quiz
    fields = ('Status',)
    context_object_name = 'quiz'
    template_name = 'classroom/teachers/quiz_change_form2.html'

    success_url = reverse_lazy('status:quiz_rev')


class QuizListView2(ListView):
    model = Quiz
    ordering = ('name',)
    context_object_name = 'quizzes'
    template_name = 'classroom/teachers/quiz_change_list.html'

    def get_queryset(self):
        queryset = self.request.user.quizzes \
            .select_related('subject')

        return queryset