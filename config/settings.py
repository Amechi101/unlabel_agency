from .base_settings import *

PRODUCTION = True

if PRODUCTION == True:
    from .production_settings import *
else:
    from .local_settings import *

