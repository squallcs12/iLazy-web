from django.contrib.auth import get_user_model
from rest_framework import test


class APITestCase(test.APITestCase):
    """Test app run via API request
    """

    User = get_user_model()

    def login(self, user):
        self.client.login(username=user.username, password=user.raw_password)

    def error_messages(self, response):
        return [o['message'] for o in response.data['errors']]

    def error_message_codes(self, response):
        return [o['code'] for o in response.data['errors']]
