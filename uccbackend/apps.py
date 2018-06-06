from django.apps import AppConfig

class UCCBackend(AppConfig):
    name = 'unlabel_app.uccbackend'
    verbose_name = "Unlabel Backend"

    def ready(self):
        """Override this to put in:
            Users system checks
            Users signal registration
        """
        pass