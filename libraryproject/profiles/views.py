# from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import CreateView

from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Visitor, Student
from .forms import VisitorsForm, StudentForm

# Create your views here.


class NewVisitor(LoginRequiredMixin, CreateView):
    model = Visitor
    template_name = "profiles/new_visitor.html"
    form_class = VisitorsForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = self.request.user
        form.instance.user = user
        return super(NewVisitor, self).form_valid(form)


class NewStudent(LoginRequiredMixin, CreateView):
    model = Student
    template_name = "profiles/new_student.html"
    form_class = StudentForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = self.request.user
        form.instance.user = user
        return super(NewStudent, self).form_valid(form)
