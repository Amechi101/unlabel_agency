from django.apps import AppConfig

class UnlabelBackend(AppConfig):
    name = 'unlabel_agency.unlabel_backend'
    verbose_name = "Unlabel Backend"

    def ready(self):
        """Override this to put in:
            Users system checks
            Users signal registration
        """
        pass