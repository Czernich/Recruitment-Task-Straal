import requests

def convert_currency(amount,code, date):

    if code != "PLN":
        URL = f"http://api.nbp.pl/api/exchangerates/rates/a/{code}/{date}/"
        r = requests.get(URL, auth=('user', 'pass'))
        mid = r.json()["rates"][0]["mid"]
    else:
        mid = 1

    amount_in_pln = amount* mid

    return int(amount_in_pln)

