# -*- coding: utf-8 -*-
from django.test import TestCase
from ibantools import models
from ibantools import utils


class ValidateBicTestCase(TestCase):

    def setUp(self):
        models.BankCodeDE.objects.create(
            bic='MARKDEF1100'
        )

    def test_valid_bic_number(self):
        self.assertTrue(utils.validate_bic('MARKDEF1100'))

    def test_invalid_bic_numbers(self):
        self.assertFalse(utils.validate_bic('MARKDEF1101'))
        self.assertFalse(utils.validate_bic('as!d'))
        self.assertFalse(utils.validate_bic('asd'))


class ValidateIBANTestCase(TestCase):

    def test_valid_iban_number(self):
        self.assertTrue(utils.validate_iban('DE08700901001234567890'))

    def test_invalid_iban_number(self):
        self.assertFalse(utils.validate_iban('DE08700901001234567891'))
        self.assertFalse(utils.validate_iban('asd!'))
        self.assertFalse(utils.validate_iban('asd'))


class ValidateIBANGenerationTestCase(TestCase):

    def test_success_generation(self):
        self.assertEquals(
            utils.get_iban_by_bank_account(
                account_number='70001506',
                bank_number='70000000'),
            'DE05700000000070001506'
        )

    def test_unsupported_country(self):
        with self.assertRaises(ValueError):
            utils.get_iban_by_bank_account(
                country='US',
                account_number='70001506',
                bank_number='70000000'
            )

    def test_invalid_account_numbers(self):
        with self.assertRaises(ValueError):
            utils.get_iban_by_bank_account(
                account_number='!123123132123',
                bank_number='70000000'
            )

        with self.assertRaises(ValueError):
            utils.get_iban_by_bank_account(
                account_number='123',
                bank_number='70000000'
            )

    def test_invalid_bank_numbers(self):
        with self.assertRaises(ValueError):
            utils.get_iban_by_bank_account(
                account_number='70001506',
                bank_number='!70000000'
            )

        with self.assertRaises(ValueError):
            utils.get_iban_by_bank_account(
                account_number='70001506',
                bank_number='1'
            )
