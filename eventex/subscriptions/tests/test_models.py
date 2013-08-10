# coding: utf-8
from django.test import TestCase
from django.db import IntegrityError
from datetime import datetime
from eventex.subscriptions.models import Subscription

class SubscriptionTest(TestCase):
    def setUp(self):
        self.obj = Subscription(
            name='Hugo Leonardo Costa e Silva',
            cpf='01624428665',
            email='hugoleodev@gmail.com',
            phone='3288258109'
        )

    def test_create(self):
        'Subscription must have name, cpf, email, phone'
        self.obj.save()
        self.assertEquals(1, self.obj.id)

    def test_has_created_at(self):
        'Subscription must have automatic created_at'
        self.obj.save()
        self.assertIsInstance(self.obj.created_at, datetime)

    def test_unicode(self):
        'Subscription must have name field as unicode'
        self.assertEquals(u'Hugo Leonardo Costa e Silva', unicode(self.obj))
        
    def test_paid_default_value_is_False(self):
        'By default paid must be false'
        self.assertEqual(False, self.obj.paid)


class SubscriptionUniqueTest(TestCase):
    def setUp(self):
        Subscription.objects.create(
            name='Hugo Leonardo Costa e Silva',
            cpf='01624428665',
            email='hugoleodev@gmail.com',
            phone='3288258109'
        )

    def test_cpf_unique(self):
        'CPF must be unique'
        subscription = Subscription(
            name='Hugo Silva',
            cpf='01624428665',
            email='hugosilva@gmail.com',
            phone='3291386511'
        )
        self.assertRaises(IntegrityError, subscription.save)

    def test_email_unique(self):
        'Email must be unique'
        subscription = Subscription(
            name='Hugo Silva',
            cpf='01624428600',
            email='hugoleodev@gmail.com',
            phone='3291386511'
        )
        self.assertRaises(IntegrityError, subscription.save)