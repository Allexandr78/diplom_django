''' Модуль приложения user '''
from django.apps import AppConfig


class UserConfig(AppConfig):
    ''' Класс приложения user '''
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'user'

    def ready(self):
        import user.signals