====
Bank
====

Bank ist eine App zum verifizieren von IBAN und BIC Daten, sowie generieren
von IBAN Nummern aus alten Bankleitzahlen und Kontonummern


Quick start
-----------

1. Add "bank" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'bank',
    ]

2. Run `python manage.py migrate` to create the bank models.

3. Import official bank csv

    Command:
    ./manage.py import_bundesbank_bankleitzahlen ~/Downloads/blz_2015_09_07_txt.txt

    Resources:
	- http://www.bundesbank.de/Navigation/DE/Aufgaben/Unbarer_Zahlungsverkehr/Serviceangebot/Bankleitzahlen/bankleitzahlen.html
    - http://www.bundesbank.de/Redaktion/DE/Downloads/Aufgaben/Unbarer_Zahlungsverkehr/Bankleitzahlen/2016_03_06/blz_2015_12_07_txt.txt?__blob=publicationFile


Developer Hints
---------------

- python setup.py sdist
- django-admin makemessages --ignore .virtualenv --ignore fixtures -a --no-location
