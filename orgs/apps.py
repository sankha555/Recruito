from django.apps import AppConfig


class OrgsConfig(AppConfig):
    name = 'orgs'

    def ready(self):
        import orgs.signals