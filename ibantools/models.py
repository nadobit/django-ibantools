# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _


class BankCodeDE(models.Model):

    PSP_YES = '1'
    PSP_NO = '2'
    PSP_CHOICES = (
        (PSP_YES, _('Yes')),
        (PSP_NO, _('No')),
    )

    AK_NEW = 'A'
    AK_DELETED = 'D'
    AK_CHANGED = 'M'
    AK_UNCHANGED = 'U'
    AK_CHOICES = (
        (AK_NEW, _('New')),
        (AK_DELETED, _('Deleted')),
        (AK_CHANGED, _('Changed')),
        (AK_UNCHANGED, _('Unchanged')),
    )

    BBL_NS = '0'
    BBL_DP = '1'
    BBL_CHOICES = (
        (BBL_NS, _('No declaration')),
        (BBL_DP, _('Declarted for deletion')),
    )

    bank_code = models.CharField(max_length=8, verbose_name=_('Bank code'))
    payment_service_provider = models.CharField(max_length=1, choices=PSP_CHOICES, default=PSP_NO, verbose_name=_('Payment service provider'), help_text=u'Merkmal, ob bankleitzahlführender Zahlungsdienstleister („1“) oder nicht („2“)')
    description = models.CharField(max_length=58, verbose_name=_('Description'), help_text=u'Bezeichnung des Zahlungsdienstleisters (ohne Rechtsform)')
    zip_code = models.CharField(max_length=5, verbose_name=_('Zip code'))
    city = models.CharField(max_length=35, verbose_name=_('City'))
    short_description = models.CharField(max_length=27, verbose_name=_('Short description'), help_text='Kurzbezeichnung des Zahlungsdienstleisters mit Ort (ohne Rechtsform)')
    pan = models.CharField(max_length=5, verbose_name=_('PAN'), help_text=u'Institutsnummer für PAN')
    bic = models.CharField(max_length=11, verbose_name=_('BIC'), help_text=u'Business Identifier Code')
    check_digit_method = models.CharField(max_length=2, verbose_name=_('Check digit method'), help_text=u'Kennzeichen für Prüfzifferberechnungsmethode')
    dataset_number = models.CharField(max_length=6, verbose_name=_('Dataset number'), help_text=u'Nummer des Datensatzes')
    indicator_changed = models.CharField(max_length=1, verbose_name=_('Indicator changed'), choices=AK_CHOICES, default=AK_NEW, help_text=u'Änderungskennzeichen „A“ (Addition) für neue, „D“ (Deletion) für gelöschte, „U“(Unchanged) für unveränderte und „M“ (Modified) für veränderte Datensätze')
    indicator_deleted = models.CharField(max_length=1, verbose_name=_('Indicator deleted'), choices=BBL_CHOICES, default=BBL_NS, help_text=u'Hinweis auf eine beabsichtigte Bankleitzahllöschung')
    succession_bank_code = models.CharField(max_length=8, verbose_name=_('Succession bank code'), help_text=u'Hinweis auf Nachfolge-Bankleitzahl')
    iban_rule = models.CharField(max_length=6, verbose_name=_('IBAN Rule'), help_text=_(u'Kennzeichen für die IBAN-Regel'))

    class Meta:
        verbose_name = _('German Bank Code')
        verbose_name_plural = _('German Bank Codes')
        ordering = ('bank_code', )

    def __unicode__(self):
        return self.description
