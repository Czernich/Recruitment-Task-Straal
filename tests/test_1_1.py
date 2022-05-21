import unittest

import requests

from main_test import RecruitmentApp

my_app = RecruitmentApp.app_url

class RecruitmentApp(unittest.TestCase):
    def setUp(self):
        self._response = requests.get(my_app)

    def test_url_exists(self):
        self.assertIsNotNone(my_app)
        self.assertIsInstance(my_app, str)
        self.assertNotEqual(my_app, "")

    def test_status_code(self):
        self.assertEqual(self._response.status_code, 200)

    def test_response(self):
        self.assertEqual(
            self._response.json(),
            "Route directory"
        )


if __name__ == "__main__":
    unittest.main()