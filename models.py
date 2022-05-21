from pydantic import BaseModel
from typing import Union
from typing import List

class CurrencyCode(str):
    EUR = "EUR"
    USD = "USD"
    GBP = "GBP"
    PLN = "PLN"

class Type(str):
    pay_by_link = "pay_by_link"
    card = "card"
    dp = "dp"

class PBL(BaseModel):
    created_at: str
    currency: CurrencyCode
    amount: int
    description: str
    bank: str

class DP(BaseModel):
    created_at: str
    currency: CurrencyCode
    amount: int
    description: str
    iban: str

class Card(BaseModel):
    created_at: str
    currency: CurrencyCode
    amount: int
    description: str
    cardholder_name: str
    cardholder_surname: str
    card_number: str

class RequestBody(BaseModel):
    pay_by_link: List[PBL] | None = None
    dp: List[DP] | None = None
    card: List[Card] | None = None

class PaymentInfo(BaseModel):
    date: str | None = None
    type: Type | None = None
    payment_mean: str | None = None
    description: str | None = None
    currency: CurrencyCode | None = None
    amount: int | None = None
    amount_in_pln: int | None = None

# --------------------For second endpoint-------------------------
class PBLExtended(BaseModel):
    customer_id: int
    created_at: str
    currency: CurrencyCode
    amount: int
    description: str
    bank: str

class DPExtended(BaseModel):
    customer_id: int
    created_at: str
    currency: CurrencyCode
    amount: int
    description: str
    iban: str

class CardExtended(BaseModel):
    customer_id: int
    created_at: str
    currency: CurrencyCode
    amount: int
    description: str
    cardholder_name: str
    cardholder_surname: str
    card_number: str

class PaymentInfoExtended(BaseModel):
    customer_id: int | None = None
    date: str | None = None
    type: Type | None = None
    payment_mean: str | None = None
    description: str | None = None
    currency: CurrencyCode | None = None
    amount: int | None = None
    amount_in_pln: int | None = None

class RequestBodyExtended(BaseModel):
    pay_by_link: List[PBLExtended] | None = None
    dp: List[DPExtended] | None = None
    card: List[CardExtended] | None = None