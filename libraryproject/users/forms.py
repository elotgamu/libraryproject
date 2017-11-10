from django.contrib.auth.forms import UserCreationForm
from .models import User


class CreateUserForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super(CreateUserForm, self).__init__(*args, **kwargs)
        if not self.fields['type_of_user'].choices[0][0] == '':
            self.fields['type_of_user'].choices.insert(
                0, ('', 'Select the user type'))

    def signup(self, request, user):
        user.name = self.cleaned_data[
            'first_name'] + " " + self.cleaned_data['last_name']
        user.type_of_user = self.cleaned_data['type_of_user']
        user.save()

    class Meta:
        model = User
        fields = ('first_name',
                  'last_name',
                  'email',
                  'password1',
                  'password2',
                  'type_of_user',
                  )
        exclude = (
            'username',
        )
