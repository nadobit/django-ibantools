# -*- coding: utf-8 -*-
import re


def get_numeric_country_code(iso2_country_code):

    if not re.match('^[A-Z]{2}$', iso2_country_code):
        return False

    alphabet = list(map(chr, range(ord('A'), ord('Z') + 1)))
    first_letter_code = alphabet.index(iso2_country_code[:1]) + 10
    second_letter_code = alphabet.index(iso2_country_code[1:]) + 10

    return int('%d%d' % (first_letter_code, second_letter_code))
