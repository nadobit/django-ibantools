# -*- coding: utf-8 -*-
from django.contrib import admin
from ibantools.models import BankCodeDE


@admin.register(BankCodeDE)
class BankCodeDEAdmin(admin.ModelAdmin):

    list_display = (
        'bank_code',
        'description',
        'city',
        'check_digit_method',
        'bic',
    )
    list_filter = (
        'payment_service_provider',
        'indicator_changed',
        'indicator_deleted',
    )
    search_fields = (
        'description',
        'city',
        'bank_code',
        'bic',
        'zip_code',
    )

    actions_selection_counter = True
