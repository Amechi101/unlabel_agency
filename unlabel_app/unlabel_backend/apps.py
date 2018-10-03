from django.apps import AppConfig

class UnlabelBackend(AppConfig):
    name = 'unlabel_app.unlabel_backend'
    verbose_name = "Unlabel Backend"

    def ready(self):
        import unlabel_app.unlabel_backend.signals