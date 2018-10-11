from .base_settings import *

PRODUCTION = env.bool('DJANGO_PRODUCTION_BOOL', default=False)

if PRODUCTION == True:
    from .production_settings import *
else:
    from .local_settings import *

