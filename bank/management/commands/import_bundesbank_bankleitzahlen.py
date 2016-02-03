# -*- coding: utf-8 -*-
import csv
from django.core.management.base import BaseCommand
from ...models import Bankleitzahl


class Command(BaseCommand):
    help = 'Importiert Bankleitzaheln über eine von der Bundesbank gestellte CSV Datei'

    def add_arguments(self, parser):
        parser.add_argument('csvfile', type=str)

    def handle(self, *args, **options):

        Bankleitzahl.objects.all().delete()

        with open(options['csvfile'], 'rb') as csvfile:
            reader = csv.reader(csvfile)
            for line in reader:
                data = unicode(line[0], "ISO-8859-1")
                satz = Bankleitzahl.objects.create()

                satz.bankleitzahl = unicode(data[0:8]).strip()
                satz.zahlungsdienstleister = unicode(data[8:9]).strip()
                satz.bezeichnung = unicode(data[9:67]).strip()
                satz.postleitzahl = unicode(data[67:72]).strip()
                satz.ort = unicode(data[72:107]).strip()
                satz.kurzbezeichnung = unicode(data[107:134]).strip()
                satz.pan = unicode(data[134:139]).strip()
                satz.bic = unicode(data[139:150]).strip()
                satz.pruefzifferberechnungsmethode = unicode(data[150:152]).strip()
                satz.datensatz = unicode(data[152:158]).strip()
                satz.indikator_geaendert = unicode(data[158:159]).strip()
                satz.indikator_loeschung = unicode(data[159:160]).strip()
                satz.nachfolge_bankleitzahl = unicode(data[160:168]).strip()
                satz.iban_regel = unicode(data[168:174]).strip()

                satz.save()

            print "Import abgeschlossen"
