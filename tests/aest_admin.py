import unittest
import json
from app.models.views import app2


class AdminTest(unittest.TestCase):

    def setUp(self):
        self.app1 = app2.test_client()
        self.app1.testing = True