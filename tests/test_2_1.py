import unittest
import urllib.parse

import requests

from main_test import RecruitmentApp
my_app = RecruitmentApp.app_url

class RecruitmentAppSetupTest(unittest.TestCase):
    def setUp(self):
        self.app_path = urllib.parse.urljoin(my_app, "/customer-report")

# -----------------------------------------------------------------------

    def test_post(self):
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
                            "created_at": "2021-05-14T08:27:09Z",
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
            response_json = response.json()
            self.assertEqual(
                response_json,
                [
                    {
                        "customer_id": 1,
                        "date": "2021-05-14T08:27:09Z",
                        "type": "dp",
                        "payment_mean": "DE91100000000123456789",
                        "description": "FastFood",
                        "currency": "USD",
                        "amount": 599,
                        "amount_in_pln": 2238
                    },
                    {
                        "customer_id": 2,
                        "date": "2021-05-14T08:27:09Z",
                        "type": "dp",
                        "payment_mean": "DE91100000000123456789",
                        "description": "FastFood",
                        "currency": "USD",
                        "amount": 599,
                        "amount_in_pln": 2238
                    }
                ]
            )

if __name__ == "__main__":
    unittest.main()
