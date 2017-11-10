from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import Group, Permission
from .models import Librarian


def define_librarian_group(sender, **kwargs):
    group_name = 'librarian'
    permissions = [
        Permission.objects.get(codename='add_author'),
        Permission.objects.get(codename='change_author'),
        Permission.objects.get(codename='add_genre'),
        Permission.objects.get(codename='change_genre'),
        Permission.objects.get(codename='add_book'),
        Permission.objects.get(codename='change_book'),
    ]
    create_group(group_name, permissions)


def create_group(name, permissions):
    group, created = Group.objects.get_or_create(name=name)
    [group.permissions.add(permission) for permission in permissions]


def add_librarian_to_group(user):
    librarian_group = Group.objects.get(name='librarian')
    librarian_group.user_set.add(user)
    print('The new librarian has been added to the group')


@receiver(post_save, sender=Librarian)
def assign_new_librarian_to_group(sender, **kwargs):
    '''Assign the new librarian to the groups'''

    if kwargs['created'] is False:
        if kwargs['instance'].user.groups.filter(name='librarian').exists():
            '''This profile is already on his group'''
            print('This librarian is on the group')
        else:
            add_librarian_to_group(kwargs['instance'].user)
            '''Add the recently created profile'''
    else:
        add_librarian_to_group(kwargs['instance'].user)
