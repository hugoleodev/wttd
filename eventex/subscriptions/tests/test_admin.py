# coding: utf-8
from django.test import TestCase
from mock import Mock
from eventex.subscriptions.admin import SubscriptionAdmin, Subscription, admin


class MarkAsPaidTest(TestCase):
    def setUp(self):
        # Instancia o ModelAdmin
        self.model_admin = SubscriptionAdmin(Subscription, admin.site)
        
        #Popula o Banco
        Subscription.objects.create(name='Hugo Silva', cpf='00000000001',
                                    email='hugoleodev@gmail.com')
    def test_has_action(self):
        'Action is installed'
        self.assertIn('mark_as_paid', self.model_admin.actions)
    
    def test_mark_all(self):
        fake_request = Mock()
        queryset = Subscription.objects.all()
        self.model_admin.mark_as_paid(fake_request, queryset)
        self.assertEqual(1, Subscription.objects.filter(paid=True).count())