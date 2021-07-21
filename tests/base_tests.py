import unittest
import json
from app.models.views import app2
from app.models.tables import Migration
from .import REGISTER_ADMIN, ADMIN_LOGIN, REGISTER_USER, USER_LOGIN

BASE_URL = "/api/v1/"


class BaseTest(unittest.TestCase):

    """Setting up testing data for Tests."""

    def setUp(self):
        self.migration = Migration()
        self.base_url = BASE_URL
        self.app1 = app2.test_client()

    def return_admin_token(self):
        """Return admin token."""
        self.app1.post(self.base_url + "users/registration", json=REGISTER_ADMIN)
        response = self.app1.post(self.base_url + "users/login", json=ADMIN_LOGIN)
        return json.loads(response.data)['access_token']

    def return_user_token(self):
        """Return user token."""
        self.app1.post(self.base_url + "users/registration", json=REGISTER_USER)
        response = self.app1.post(self.base_url + 'users/login', json=USER_LOGIN)
        return json.loads(response.data)["access_token"]