from django.contrib import admin
from .models import Visitor, Student, Librarian
# Register your models here.


class AdminVisitor(admin.ModelAdmin):
    '''
        Admin View for Visitor
    '''
    list_display = ('visitor_name', 'visitor_email',
                    'phone', 'address', 'id_card')

    def visitor_name(self, visitor):
        return visitor.user.name

    def visitor_email(self, visitor):
        return visitor.user.email


admin.site.register(Visitor, AdminVisitor)


class StudentAdmin(admin.ModelAdmin):
    '''
        Admin View for Student
    '''
    list_display = ('student_name', 'student_email',
                    'address', 'student_number', 'school_name')

    def student_name(self, student):
        return student.user.name

    def student_email(self, student):
        return student.user.email


admin.site.register(Student, StudentAdmin)


class LibrarianAdmin(admin.ModelAdmin):
    '''
        Admin View for Librarian
    '''
    # form = LibrarianCreateForm
    list_display = ('librarian_name', 'librarian_email')

    def librarian_name(self, librarian):
        return librarian.user.name

    def librarian_email(self, librarian):
        return librarian.user.email


admin.site.register(Librarian, LibrarianAdmin)
