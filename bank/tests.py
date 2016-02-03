from django.test import TestCase
from . import models
from . import utils


class ValidateBicTestCase(TestCase):
    def setUp(self):
        models.Bankleitzahl.objects.create(
            bic='MARKDEF1100'
        )

    def test_valid_bic_numbers(self):
        self.assertTrue(utils.validate_bic('MARKDEF1100'))

    def test_invalid_bic_numbers(self):
        self.assertFalse(utils.validate_bic('MARKDEF1101'))
        self.assertFalse(utils.validate_bic('as!d'))
        self.assertFalse(utils.validate_bic('asd'))
