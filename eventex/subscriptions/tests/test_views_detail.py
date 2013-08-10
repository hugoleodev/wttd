# coding: utf-8
from django.test import TestCase
from eventex.subscriptions.models import Subscription
from django.core.urlresolvers import reverse as r

class DetailTest(TestCase):
    def setUp(self):
        subscription = Subscription.objects.create(name="Hugo Leonardo Costa e Silva",
                                                   cpf="01624428665",
                                                   email="hugoleodev@gmail.com",
                                                   phone="32-08080808")
        self.resp = self.client.get(r('subscriptions:detail', args=[subscription.pk]))

    def test_get(self):
        'GET /inscricao/1/ should return status 200'
        self.assertEqual(200, self.resp.status_code)

    def test_tempate(self):
        'Uses Template'
        self.assertTemplateUsed(self.resp,
                                'subscriptions/subscription_detail.html')

    def test_context(self):
        'Context mist have a subscription instance.'
        subscription = self.resp.context['subscription']
        self.assertIsInstance(subscription, Subscription)

    def test_html(self):
        'Check if subscription data was rendered.'
        self.assertContains(self.resp, "Hugo Leonardo Costa e Silva")


class DetailViewNotFound(TestCase):
    def test_not_found(self):
        response = self.client.get(r('subscriptions:detail', args=[0]))
        self.assertEqual(404, response.status_code)
