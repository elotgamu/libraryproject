from django.conf.urls import url

from .views import NewVisitor, NewStudent

urlpatterns = [
    url(r'^registro-visitante/$', NewVisitor.as_view(), name='new-visitor'),
    url(r'^registro-estudiante/$', NewStudent.as_view(), name='new-student'),
]
