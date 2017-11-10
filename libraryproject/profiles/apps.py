from django.apps import AppConfig

from django.db.models.signals import post_migrate


class ProfilesConfig(AppConfig):
    name = 'libraryproject.profiles'
    verbose_name = "Profiles"

    def ready(self):
        from . import signals
        post_migrate.connect(signals.define_librarian_group, sender=self)
