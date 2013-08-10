# coding: utf-8
from eventex.subscriptions.forms import SubscriptionForm
from django.test import TestCase
from django.core.urlresolvers import reverse as r


class SubscriptionFormTest(TestCase):

    def setUp(self):
        self.resp = self.client.get(r('subscriptions:subscribe'))

    def test_has_form(self):
        'Context must have the subscription form'
        form = self.resp.context['form']
        self.assertIsInstance(form, SubscriptionForm)

    def test_form_has_fields(self):
        'Form must have 4 fields'
        form = self.resp.context['form']
        self.assertItemsEqual(['name', 'email', 'cpf', 'phone'], form.fields)