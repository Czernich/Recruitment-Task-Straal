import unittest
import urllib.parse

import requests

from main_test import RecruitmentApp
my_app = RecruitmentApp.app_url

class RecruitmentAppSetupTest(unittest.TestCase):
    def setUp(self):
        self.app_path = urllib.parse.urljoin(my_app, "/report")

# -----------------------------------------------------------------------

    def test_post(self):
            response = requests.post(
                self.app_path, json={"pay_by_link": [
                {
                "created_at": "2021-05-13T01:01:43-08:00",
                "currency":" EUR",
                "amount": 3000,
                "description": "Gym membership",
                "bank": "mbank"
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
                        "date": "2021-05-13T09:01:43Z",
                        "type": "pay_by_link",
                        "description": "Gym membership",
                        "currency": " EUR",
                        "amount": 3000,
                        "amount_in_pln": 13634,
                        "payment_mean": "mbank"
                    }
                ]
            )

# -----------------------------------------------------------------------

    def test_incorrect_date(self):
        retrive_response = requests.post(
            self.app_path, json={"dp": [
            {
            "created_at": "2021-13-14XX",
            "currency": "USD",
            "amount": 599,
            "description": "FastFood",
            "iban": "DE91100000000123456789"
            }
        ]
    }
        )
        self.assertEqual(retrive_response.status_code, 400)

# -----------------------------------------------------------------------

    def test_sort(self):
        response = requests.post(
            self.app_path, json={
                "pay_by_link": [
                        {
                        "created_at": "2021-05-13T01:01:43-08:00",
                        "currency":" EUR",
                        "amount": 3000,
                        "description": "Gym membership",
                        "bank": "mbank"
                        }
                ],
                "dp": [
                        {
                        "created_at": "2021-05-14T08:27:09Z",
                        "currency": "USD",
                        "amount": 599,
                        "description": "FastFood",
                        "iban": "DE91100000000123456789"
                        }
                ],
                "card": [
                        {
                        "created_at": "2021-05-13T09:00:05+02:00",
                        "currency": "PLN",
                        "amount": 2450,
                        "description": "REF123457",
                        "cardholder_name": "John",
                        "cardholder_surname": "Doe",
                        "card_number": "2222222222222222"
                        },
                        {
                        "created_at": "2021-05-14T18:32:26Z",
                        "currency": "GBP",
                        "amount": 1000,
                        "description": "REF123456",
                        "cardholder_name": "John",
                        "cardholder_surname": "Doe",
                        "card_number": "1111111111111111"
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
        "date": "2021-05-13T07:00:05Z",
        "type": "card",
        "description": "REF123457",
        "currency": "PLN",
        "amount": 2450,
        "amount_in_pln": 2450,
        "payment_mean": "John Doe 2222********2222"
    },
    {
        "date": "2021-05-13T09:01:43Z",
        "type": "pay_by_link",
        "description": "Gym membership",
        "currency": " EUR",
        "amount": 3000,
        "amount_in_pln": 13634,
        "payment_mean": "mbank"
    },
    {
        "date": "2021-05-14T08:27:09Z",
        "type": "dp",
        "description": "FastFood",
        "currency": "USD",
        "amount": 599,
        "amount_in_pln": 2238,
        "payment_mean": "DE91100000000123456789"
    },
    {
        "date": "2021-05-14T18:32:26Z",
        "type": "card",
        "description": "REF123456",
        "currency": "GBP",
        "amount": 1000,
        "amount_in_pln": 5257,
        "payment_mean": "John Doe 1111********1111"
    }
]
        )



if __name__ == "__main__":
    unittest.main()
