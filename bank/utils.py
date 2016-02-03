import re
from . import models


def validate_bic(bic):

    if not re.match('^[a-zA-Z0-9_]{,11}$', bic):
        return False

    bic = bic.upper()
    count = len(models.Bankleitzahl.objects.filter(bic=bic))
    return count
    return True if count > 0 else False
