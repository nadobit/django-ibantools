# -*- coding: utf-8 -*-
from django.contrib import admin
from . import models


@admin.register(models.Bankleitzahl)
class BankleitzahlAdmin(admin.ModelAdmin):
    readonly_fields = ()
    list_display = (
        'bankleitzahl',
        'bezeichnung',
        'ort',
        'pruefzifferberechnungsmethode',
    )
    list_filter = (
        'zahlungsdienstleister',
        'indikator_geaendert',
        'indikator_loeschung',
    )
    search_fields = (
        'bezeichnung',
        'ort'
    )
    ordering = ()
    actions_selection_counter = True
