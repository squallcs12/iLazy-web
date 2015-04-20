from datetime import timedelta
from django.utils import timezone
from faker import Faker
from rest_framework import status

from accounts.factories import UserFactory
from api.factories import AppFactory, UserAppFactory
from api.models import UserApp
from api.tests.core import APITestCase


fake = Faker()


class AppPurchaseViewTestCase(APITestCase):
    """Test app run via API request
    """

    def setUp(self):
        self.user = UserFactory()
        # make sure enough coins to buy
        self.app = AppFactory(price=self.user.coins - 1, price_life=self.user.coins)
        self.login(self.user)

    def test_purchase_success(self):

        response = self.client.post('/api/purchase/', {
            'app': self.app.id
        })
        response.status_code.should.equal(status.HTTP_200_OK)
        response.data['success'].should.be.true

        UserApp.objects.filter(user=self.user, app=self.app).count().should.equal(1)
        user_app = UserApp.objects.get(user=self.user, app=self.app)
        (user_app.expires - timezone.now().date()).days.should.equal(30)

        self.User.objects.get(pk=self.user.id).coins.should.equal(1)

    def test_purchase_success_life(self):
        response = self.client.post('/api/purchase/', {
            'app': self.app.id,
            'kind': 'life',
        })
        response.status_code.should.equal(status.HTTP_200_OK)

        user_app = UserApp.objects.get(user=self.user, app=self.app)
        user_app.expires.should.be.none

        self.User.objects.get(pk=self.user.id).coins.should.equal(0)

    def test_purchase_fail_not_enough_coins(self):
        UserApp.objects.filter(user=self.user, app=self.app).count().should.equal(0)

        self.app.price = self.user.coins + 1
        self.app.save()

        response = self.client.post('/api/purchase/', {
            'app': self.app.id
        })
        response.status_code.should.equal(status.HTTP_402_PAYMENT_REQUIRED)
        self.error_messages(response).should.contain("You need more 1 coin(s) to buy this app.")
        self.error_message_codes(response).should.contain("NOT_ENOUGH_COINS")

    def test_purchase_duplicate_extend_usage_time(self):
        user_app = UserAppFactory(user=self.user, app=self.app)

        response = self.client.post('/api/purchase/', {
            'app': self.app.id
        })
        response.status_code.should.equal(status.HTTP_200_OK)
        response.data['success'].should.be.true

        expires = UserApp.objects.get(pk=user_app.pk).expires
        diff = expires - user_app.expires
        diff.days.should.equal(30)

    def init_expired(self):
        expired_date = timezone.now().date() - timedelta(days=1)
        self.user_app = UserAppFactory(user=self.user, app=self.app, expires=expired_date)

    def test_purchase_life_after_expired(self):
        self.init_expired()
        self.test_purchase_success_life()

    def test_purchase_expired_app_renew_expires(self):
        self.init_expired()
        self.test_purchase_success()

    def test_purchase_life_after_month(self):
        response = self.client.post('/api/purchase/', {
            'app': self.app.id,
        })
        response.status_code.should.equal(status.HTTP_200_OK)

        self.user.coins = self.app.price_life
        self.user.save()

        response = self.client.post('/api/purchase/', {
            'app': self.app.id,
            'kind': 'life',
        })
        response.status_code.should.equal(status.HTTP_200_OK)
        response.data['success'].should.be.true

        user_app = UserApp.objects.get(user=self.user, app=self.app)
        user_app.expires.should.be.none
        self.User.objects.get(pk=self.user.id).coins.should.equal(self.app.price)

    def test_purchase_life_after_month_with_just_enough_coins(self):
        response = self.client.post('/api/purchase/', {
            'app': self.app.id,
        })
        response.status_code.should.equal(status.HTTP_200_OK)

        response = self.client.post('/api/purchase/', {
            'app': self.app.id,
            'kind': 'life',
        })
        response.status_code.should.equal(status.HTTP_200_OK)
        self.User.objects.get(pk=self.user.id).coins.should.equal(0)
