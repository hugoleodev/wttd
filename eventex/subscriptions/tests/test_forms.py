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
        
    def test_cpf_is_digit(self):
        'CPF only accept digit'
        form = self.make_validated_form(cpf='BCDEA678901')
        self.assertItemsEqual(['cpf'], form.errors)
        
    def test_cpf_has_11_digits(self):
        'CPF must have 11 digits'
        form = self.make_validated_form(cpf='8901')
        self.assertItemsEqual(['cpf'], form.errors)
        
    def test_email_is_optional(self):
        'Email is optional.'
        form = self.make_validated_form(email='')
        self.assertFalse(form.errors)
        
    def test_name_must_be_capitalized(self):
        'Name must be capitalized'
        form = self.make_validated_form(name='HUGO leonardo')
        self.assertEqual('Hugo Leonardo', form.cleaned_data['name'])
        
    def test_must_inform_email_or_phone(self):
        'Email or phone are optional, but one must be informed'
        form = self.make_validated_form(email='', phone_0='', phone_1='')
        self.assertItemsEqual(['__all__'], form.errors)
    
    def make_validated_form(self, **kwargs):
        data = dict(name='Hugo Leonardo', email='hugoleodev@gmail.com',
                    cpf='12345678901', phone_0='32', phone_1='91386511')
        data.update(kwargs)
        form = SubscriptionForm(data)
        form.is_valid()
        return form

