from faker import Faker
import mock

from accounts.factories import UserFactory
from api.factories import AppFactory, UserAppFactory
from api.models import Result
from api.tests.core import APITestCase


fake = Faker()


class AppExecuteViewTestCase(APITestCase):
    """Test app run via API request
    """

    def setUp(self):
        self.user = UserFactory()
        self.app = AppFactory()
        UserAppFactory(user=self.user, app=self.app)
        self.login(self.user)

    def test_result_row_is_created(self):
        count = Result.objects.all().count()
        self.client.post("/api/execute/", {
            "app": self.app.id,
        })
        Result.objects.all().count().should.equal(count + 1)

    def test_result_id_is_returned(self):
        response = self.client.post("/api/execute/", {
            "app": self.app.id,
        })
        response.data['result']['id'].should.equal(Result.objects.all().latest("id").id)

    def test_task_is_sent(self):
        with mock.patch("api.views.app_execute_view.execute_app") as mock_obj:
            self.client.post("/api/execute/", {
                "app": self.app.id,
            })
            result = Result.objects.all().latest("id")
            mock_obj.delay.assert_called_with(result.id, json_params='')

    def test_task_is_sent_with_parameter(self):
        with mock.patch("api.views.app_execute_view.execute_app") as mock_obj:
            json_params = fake.name()
            self.client.post("/api/execute/", {
                "app": self.app.id,
                "json_params": json_params,
            })
            result = Result.objects.all().latest("id")
            mock_obj.delay.assert_called_with(result.id, json_params=json_params)

    def test_non_login_run_throw_exception(self):
        self.client.logout()
        response = self.client.post("/api/execute/", {
            "app": self.app.id,
        })
        response.status_code.should.equal(401)

    def test_non_own_app_run_throw_exception(self):
        user = UserFactory()
        self.client.logout()
        self.login(user)
        response = self.client.post("/api/execute/", {
            "app": self.app.id,
        })
        response.status_code.should.equal(401)
        response.data.should.contain('errors')
        self.error_messages(response).should.contain("You need to own this application before using it.")
