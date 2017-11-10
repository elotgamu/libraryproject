from django.conf import settings
from allauth.account.adapter import DefaultAccountAdapter
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from django.contrib import messages


class AccountAdapter(DefaultAccountAdapter):

    def is_open_for_signup(self, request):
        return getattr(settings, 'ACCOUNT_ALLOW_REGISTRATION', True)

    def get_login_redirect_url(self, request):
        user = self.request.user
        home = '/'

        if user.is_visitor():
            if user.has_visitor_profile():
                url = home
            else:
                url = '/profiles/registro-visitante'
        elif user.is_student():
            if user.has_student_profile():
                url = home
            else:
                url = '/profiles/registro-estudiante'
        else:
            if user.has_librarian_profile():
                url = home
            else:
                url = home
                messages.info(
                    request,
                    'Su perfil debe ser completado por otro encargado')

        return url


class SocialAccountAdapter(DefaultSocialAccountAdapter):

    def is_open_for_signup(self, request, sociallogin):
        return getattr(settings, 'ACCOUNT_ALLOW_REGISTRATION', True)
