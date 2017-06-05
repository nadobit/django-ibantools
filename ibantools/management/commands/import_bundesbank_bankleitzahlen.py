# -*- coding: utf-8 -*-
import csv
from django.core.management.base import BaseCommand
from ...models import BankCodeDE


class Command(BaseCommand):
    help = 'Importiert Bankleitzaheln über eine von der Bundesbank gestellte CSV Datei'

    def add_arguments(self, parser):
        parser.add_argument('csvfile', type=str)

    def handle(self, *args, **options):

        BankCodeDE.objects.all().delete()
        csv.register_dialect('bundesbank', delimiter='|', quoting=csv.QUOTE_NONE)

        with open(options['csvfile'], 'rb') as csvfile:
            reader = csv.reader(csvfile, 'bundesbank')
            for line in reader:
                data = unicode(''.join(line), "ISO-8859-1")
                satz = BankCodeDE.objects.create()

                satz.bank_code = unicode(data[0:8]).strip()
                satz.payment_service_provider = unicode(data[8:9]).strip()
                satz.description = unicode(data[9:67]).strip()
                satz.zip_code = unicode(data[67:72]).strip()
                satz.city = unicode(data[72:107]).strip()
                satz.short_description = unicode(data[107:134]).strip()
                satz.pan = unicode(data[134:139]).strip()
                satz.bic = unicode(data[139:150]).strip()
                satz.check_digit_method = unicode(data[150:152]).strip()
                satz.dataset_number = unicode(data[152:158]).strip()
                satz.indicator_changed = unicode(data[158:159]).strip()
                satz.indicator_deleted = unicode(data[159:160]).strip()
                satz.succession_bank_code = unicode(data[160:168]).strip()
                satz.iban_rule = unicode(data[168:174]).strip()

                satz.save()

            print "Import Done"
