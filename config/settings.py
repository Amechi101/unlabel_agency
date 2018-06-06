from .base_settings import *

PRODUCTION = False

if PRODUCTION == True:
    from .production_settings import *
else:
    from .local_settings import *

