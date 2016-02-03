import re
from . import models
from . import operations


def validate_bic(bic):

    if not re.match('^[a-zA-Z0-9_]{,11}$', bic):
        return False

    bic = bic.upper()
    count = len(models.Bankleitzahl.objects.filter(bic=bic))

    return True if count > 0 else False


def validate_iban(iban):

    iban = iban.upper()
    if not re.match('^[A-Z]{2}[A-Z0-9]{20}$', iban):
        return False

    checksum = int("%s%d%s" % (
        iban[4:],
        operations.get_numeric_country_code(iban[:2]),
        iban[2:4],
    ))

    mod_result = checksum % 97

    return mod_result == 1
