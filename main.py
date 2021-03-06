from unittest import result
from fastapi import FastAPI, Response
from starlette import status

from models import *
from datetime_val import *
from currency_conv import *
from results import *

app = FastAPI()

app.last_user_report = []

@app.get("/")
def route():
    return "Route directory"


@app.post("/report")
def report_transaction(request_body: RequestBody, response: Response):
    item_dict = request_body.dict()
    results_list = []
    
    for key in item_dict.keys():
        if item_dict[key] != None:
            for dict in item_dict[key]:
                payment_info = PaymentInfo()

                if not check_date(dict["created_at"]):
                    response.status_code = status.HTTP_400_BAD_REQUEST
                    return response
                else:
                    curr_date = standarize_date(dict["created_at"])
                    payment_info.date = curr_date
                    payment_info.type = key
                    payment_info.description = dict["description"]
                    payment_info.currency = dict["currency"]
                    payment_info.amount = dict["amount"]

                    if dict["currency"] != "PLN":
                        simple_date = curr_date[:10]
                        amount_in_pln = convert_currency(int(dict["amount"]), dict["currency"].strip(),simple_date)
                    else:
                        amount_in_pln = dict["amount"]

                    payment_info.amount_in_pln = amount_in_pln

                    if key == "pay_by_link":
                        payment_info.payment_mean = dict["bank"]
                    elif key == "dp":
                        payment_info.payment_mean = dict["iban"]
                    elif key == "card":
                        hashed_card_number = dict["card_number"][:4] + "*"*8 + dict["card_number"][12:]
                        payment_mean = dict["cardholder_name"] + " " + dict["cardholder_surname"] + " " + hashed_card_number
                        payment_info.payment_mean = payment_mean
                    else:
                        response.status_code = status.HTTP_400_BAD_REQUEST
                        return response
                    
                    results_list.append(payment_info)

    datetime_sort(results_list)
    return results_list


@app.post("/customer-report")
def customer_report(request_body: RequestBodyExtended, response: Response):
    item_dict = request_body.dict()
    results_list = []
    
    for key in item_dict.keys():
        if item_dict[key] != None:
            for dict in item_dict[key]:
                payment_info_extended = PaymentInfoExtended()

                if not check_date(dict["created_at"]):
                    response.status_code = status.HTTP_400_BAD_REQUEST
                    return response
                else:
                    curr_date = standarize_date(dict["created_at"])
                    payment_info_extended.customer_id = dict["customer_id"]
                    payment_info_extended.date = curr_date
                    payment_info_extended.type = key
                    payment_info_extended.description = dict["description"]
                    payment_info_extended.currency = dict["currency"]
                    payment_info_extended.amount = dict["amount"]

                    if dict["currency"] != "PLN":
                        simple_date = curr_date[:10]
                        amount_in_pln = convert_currency(int(dict["amount"]), dict["currency"].strip(),simple_date)
                    else:
                        amount_in_pln = dict["amount"]

                    payment_info_extended.amount_in_pln = amount_in_pln

                    if key == "pay_by_link":
                        payment_info_extended.payment_mean = dict["bank"]
                    elif key == "dp":
                        payment_info_extended.payment_mean = dict["iban"]
                    elif key == "card":
                        hashed_card_number = dict["card_number"][:4] + "*"*8 + dict["card_number"][12:]
                        payment_mean = dict["cardholder_name"] + " " + dict["cardholder_surname"] + " " + hashed_card_number
                        payment_info_extended.payment_mean = payment_mean
                    else:
                        response.status_code = status.HTTP_400_BAD_REQUEST
                        return response

                    results_list.append(payment_info_extended)

    if len(app.last_user_report) != 0:
        results_list.extend(app.last_user_report)
        app.last_user_report = []
    datetime_sort(results_list)
    
    app.last_user_report = get_last_users_report(results_list, app)

    return app.last_user_report


@app.get("/customer-report/{customer_id}")
def search_customer(customer_id, response: Response):
    results_list = []

    try:
        customer_id = int(customer_id)

    except ValueError:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return response
    
    else:
        if len(app.last_user_report) != 0:
            for i in range(len(app.last_user_report)):
                if app.last_user_report[i].customer_id == customer_id:
                    results_list.append(app.last_user_report[i])
        else:
            response.status_code = status.HTTP_404_NOT_FOUND
            return response        
        
        if len(results_list) == 0:
            response.status_code = status.HTTP_404_NOT_FOUND
            return response
        else:
            return results_list


    
    

