from django.apps import AppConfig

class UnlabelBackend(AppConfig):
    name = 'unlabel_backend'
    verbose_name = "Unlabel Backend"

    def ready(self):
        import unlabel_backend.signals