from django.apps import AppConfig


class ApplicationsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'next_active.applications'

    def ready(self):
        import next_active.applications.signals
