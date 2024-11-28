from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'next_active.accounts'

    def ready(self):
        import next_active.accounts.signals