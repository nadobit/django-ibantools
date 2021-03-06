# Generated by Django 2.0.7 on 2018-07-29 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ibantools', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bankcodede',
            name='indicator_changed',
            field=models.CharField(choices=[('A', 'New'), ('D', 'Deleted'), ('M', 'Changed'), ('U', 'Unchanged')], default='A', help_text='Änderungskennzeichen „A“ (Addition) für neue, „D“ (Deletion) für gelöschte, „U“(Unchanged) für unveränderte und „M“ (Modified) für veränderte Datensätze', max_length=1, verbose_name='Indicator changed'),
        ),
        migrations.AlterField(
            model_name='bankcodede',
            name='indicator_deleted',
            field=models.CharField(choices=[('0', 'No declaration'), ('1', 'Declarted for deletion')], default='0', help_text='Hinweis auf eine beabsichtigte Bankleitzahllöschung', max_length=1, verbose_name='Indicator deleted'),
        ),
        migrations.AlterField(
            model_name='bankcodede',
            name='payment_service_provider',
            field=models.CharField(choices=[('1', 'Yes'), ('2', 'No')], default='2', help_text='Merkmal, ob bankleitzahlführender Zahlungsdienstleister („1“) oder nicht („2“)', max_length=1, verbose_name='Payment service provider'),
        ),
        migrations.AlterField(
            model_name='bankcodede',
            name='short_description',
            field=models.CharField(help_text='Kurzbezeichnung des Zahlungsdienstleisters mit Ort (ohne Rechtsform)', max_length=27, verbose_name='Short description'),
        ),
    ]
