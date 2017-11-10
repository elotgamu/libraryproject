from django import forms

from .models import Visitor, Student, Librarian


class VisitorsForm(forms.ModelForm):

    class Meta:
        model = Visitor
        fields = ('address',
                  'phone',
                  'id_card'
                  )


class StudentForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = ('address',
                  'phone',
                  'id_card',
                  'student_number',
                  'school_name',
                  )


class LibrarianForm(forms.ModelForm):
    class Meta:
        model = Librarian
        fields = ('user',
                  'address',
                  'phone',
                  'id_card',
                  )
