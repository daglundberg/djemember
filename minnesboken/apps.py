from __future__ import unicode_literals

from django.apps import AppConfig


class MinnesbokenConfig(AppConfig):
    name = 'minnesboken'

    def ready(self):
        import minnesboken.signals
