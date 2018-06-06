from django.apps import AppConfig

class Products(AppConfig):
    name = 'unlabel_app.products'
    verbose_name = "Products"

    def ready(self):
        """Override this to put in:
            Users system checks
            Users signal registration
        """
        pass
