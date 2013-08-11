# coding: utf-8
from django.test import TestCase
from eventex.subscriptions.models import Subscription
from django.core.urlresolvers import reverse as r


class SubscribeTest(TestCase):
    def setUp(self):
        self.resp = self.client.get(r('subscriptions:subscribe'))
    
    def test_get(self):
        'GET /inscricao/ must return status code 200.'
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        'Response should be a rendered template'
        self.assertTemplateUsed(self.resp, 
                                'subscriptions/subscription_form.html')

    def test_html(self):
        'Html must contain input controls'
        self.assertContains(self.resp, '<form')
        self.assertContains(self.resp, '<input', 6)
        self.assertContains(self.resp, 'type="text"', 5)
        self.assertContains(self.resp, '<button type="submit"')

    def test_csrf(self):
        'Html must contain csrf token'
        self.assertContains(self.resp, 'csrfmiddlewaretoken')


class SubscribePostTest(TestCase):
    def setUp(self):
        data = dict(
            name='Hugo Leonardo Costa e Silva',
            cpf='01624428665',
            email='hugoleodev@gmail.com',
            phone='3288258109'
        )
        self.resp = self.client.post(r('subscriptions:subscribe'), data)

    def test_post(self):
        'Valid post should redirect to /inscricao/1/'
        self.assertEqual(302, self.resp.status_code)
        
    def test_save(self):
        'Valid post must be saved.'
        self.assertTrue(Subscription.objects.exists())

class SubscribeInvalidPostTest(TestCase):
    def setUp(self):
        data = dict(
            name='Hugo Leonardo Costa e Silva',
            cpf='0162442866500',
            email='hugoleodev@gmail.com',
            phone='3288258109'
        )
        self.resp = self.client.post(r('subscriptions:subscribe'), data)

    def test_post(self):
        'Invalid POST should not redirect'
        self.assertEqual(200, self.resp.status_code)

    def test_form_errors(self):
        'Form must contain errors'
        self.assertFalse(self.resp.context['form'].is_valid())

    def test_dont_save(self):
        'Do not save data'
        self.assertFalse(Subscription.objects.exists())
        
class TemplateRegressionTest(TestCase):
    def test_template_has_non_field_errors(self):
        'Check if non_field_errors are shown in template.'
        invalid_data = dict(name='Hugo Leonardo', cpf='00000000001')
        response = self.client.post(r('subscriptions:subscribe'), invalid_data)
        
        self.assertContains(response, '<ul class="errorlist">')
