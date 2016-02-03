# -*- coding: utf-8 -*-
from django.db import models


class Bankleitzahl(models.Model):

    ZD_JA = '1'
    ZD_NEIN = '2'
    ZD_AUSWAHL = (
        (ZD_JA, 'Ja'),
        (ZD_NEIN, 'Nein'),
    )

    AK_NEU = 'A'
    AK_GELOESCHT = 'D'
    AK_VERAENDERT = 'M'
    AK_UNVERAENDERT = 'U'
    AK_AUSWAHL = (
        (AK_NEU, 'Neu'),
        (AK_GELOESCHT, 'Gelöscht'),
        (AK_VERAENDERT, 'Verändert'),
        (AK_UNVERAENDERT, 'Unverändert'),
    )

    BBL_KA = '0'
    BBL_LV = '1'
    BBL_AUSWAHL = (
        (BBL_KA, 'Keine Angabe'),
        (BBL_LV, 'Zur Löschung vorgesehen'),
    )

    bankleitzahl = models.CharField(max_length=8)
    zahlungsdienstleister = models.CharField(max_length=1, choices=ZD_AUSWAHL, default=ZD_NEIN, help_text='Merkmal, ob bankleitzahlführender Zahlungsdienstleister („1“) oder nicht („2“)')
    bezeichnung = models.CharField(max_length=58, help_text='Bezeichnung des Zahlungsdienstleisters (ohne Rechtsform)')
    postleitzahl = models.CharField(max_length=5)
    ort = models.CharField(max_length=35)
    kurzbezeichnung = models.CharField(max_length=27, help_text='Kurzbezeichnung des Zahlungsdienstleisters mit Ort (ohne Rechtsform)')
    pan = models.CharField(max_length=5, help_text='Institutsnummer für PAN')
    bic = models.CharField(max_length=11, help_text='Business Identifier Code')
    pruefzifferberechnungsmethode = models.CharField(max_length=2, help_text='Kennzeichen für Prüfzifferberechnungsmethode', verbose_name='Berechnungsmethode')
    datensatz = models.CharField(max_length=6, help_text='Nummer des Datensatzes')
    indikator_geaendert = models.CharField(max_length=1, choices=AK_AUSWAHL, default=AK_NEU, help_text='Änderungskennzeichen „A“ (Addition) für neue, „D“ (Deletion) für gelöschte, „U“(Unchanged) für unveränderte und „M“ (Modified) für veränderte Datensätze')
    indikator_loeschung = models.CharField(max_length=1, choices=BBL_AUSWAHL, default=BBL_KA, help_text='Hinweis auf eine beabsichtigte Bankleitzahllöschung')
    nachfolge_bankleitzahl = models.CharField(max_length=8, help_text='Hinweis auf Nachfolge-Bankleitzahl')
    iban_regel = models.CharField(max_length=6, help_text='Kennzeichen für die IBAN-Regel')

    class Meta:
        verbose_name = 'Bankleitzahl'
        verbose_name_plural = 'Bankleitzahlen'
        ordering = ('bankleitzahl', )

    def __unicode__(self):
        return self.bezeichnung
