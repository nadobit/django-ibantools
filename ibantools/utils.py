# -*- coding: utf-8 -*-
import re
from . import models
from . import operations


def validate_bic(bic):

    if not re.match('^[a-zA-Z0-9_]{,11}$', bic):
        return False

    bic = bic.upper()
    count = len(models.BankCodeDE.objects.filter(bic=bic))

    return True if count > 0 else False


def validate_iban(iban):

    iban = iban.upper()
    if not re.match('^[A-Z]{2}[0-9]{20}$', iban):
        return False

    checksum = int("%s%d%s" % (
        iban[4:],
        operations.get_numeric_country_code(iban[:2]),
        iban[2:4],
    ))

    mod_result = checksum % 97

    return mod_result == 1


def get_iban_by_bank_account(account_number, bank_number, country='DE'):

    if country != 'DE':
        raise ValueError('This version only supports german iban number generation')

    if not re.match('^[0-9]{6,10}$', account_number):
        raise ValueError('Unknown account number type')

    if not re.match('^[0-9]{8}$', bank_number):
        raise ValueError('Unknown bank number type')

    account_number = "%010d" % int(account_number)
    bban = "%s%s" % (bank_number, account_number)
    country_code = operations.get_numeric_country_code(country)
    country_code_ex = "%s00" % country_code
    checksum = int("%s%s" % (bban, country_code_ex))
    mod_result = checksum % 97
    mod_checksum = "%02d" % (98 - mod_result)

    iban = "%s%s%s" % (country, mod_checksum, bban)

    return iban
