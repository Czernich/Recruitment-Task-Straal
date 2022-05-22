import unittest
import urllib.parse

import requests

from main_test import RecruitmentApp
my_app = RecruitmentApp.app_url

class RecruitmentAppSetupTest(unittest.TestCase):
    def setUp(self):
        self.app_path = urllib.parse.urljoin(my_app, "/customer-report")

    def test_get(self):
        response = requests.post(
            self.app_path, json={
                    "pay_by_link": [
                            {
                            "customer_id": 1,
                            "created_at": "2021-05-13T01:01:43-08:00",
                            "currency":" EUR",
                            "amount": 3000,
                            "description": "Gym membership",
                            "bank": "mbank"
                            }
                    ],
                    "dp": [
                            {
                            "customer_id": 1,
                            "created_at": "2021-05-20T08:27:09Z",
                            "currency": "USD",
                            "amount": 599,
                            "description": "FastFood",
                            "iban": "DE91100000000123456789"
                            },
                            {
                            "customer_id": 2,
                            "created_at": "2021-05-14T08:27:09Z",
                            "currency": "USD",
                            "amount": 599,
                            "description": "FastFood",
                            "iban": "DE91100000000123456789"
                            }
                    ]
}
        )
        self.assertEqual(response.status_code, 200)

        retrieve_response = requests.get(self.app_path + "/1")
        self.assertEqual(retrieve_response.status_code, 200)
        response_json = retrieve_response.json()
        self.assertEqual(
            response_json,
            [
                {
                    "customer_id": 1,
                    "date": "2021-05-20T08:27:09Z",
                    "type": "dp",
                    "payment_mean": "DE91100000000123456789",
                    "description": "FastFood",
                    "currency": "USD",
                    "amount": 599,
                    "amount_in_pln": 2220
                }
            ]
        )

# -----------------------------------------------------------------------

    def test_retrieve_incorrect(self):
        retrieve_response = requests.get(self.app_path + "/definitely_not_an_integer")
        self.assertEqual(retrieve_response.status_code, 400)

# -----------------------------------------------------------------------

    def test_retrieve_404(self):
        try_ids = ["/3", "/36", "/123", "2560"]
        response_404 = None
        for id in try_ids:
            retrieve_response = requests.get(self.app_path + id)
            if retrieve_response.status_code == 404:
                response_404 = retrieve_response

        self.assertEqual(response_404.status_code, 404)

if __name__ == "__main__":
    unittest.main()
