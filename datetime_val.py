from datetime import datetime
from datetime import timezone
import re
regex = r'^(-?(?:[1-9][0-9]*)?[0-9]{4})-(1[0-2]|0[1-9])-(3[01]|0[1-9]|[12][0-9])T(2[0-3]|[01][0-9]):([0-5][0-9]):([0-5][0-9])(\.[0-9]+)?(Z|[+-](?:2[0-3]|[01][0-9]):[0-5][0-9])?$'

match_iso8601 = re.compile(regex).match
def check_date(date_time):
    try:            
        if match_iso8601(date_time) is not None:
                return True
    except:
        return False
    return False


def datetime_sort(list):
    return list.sort(key = lambda payment_info:payment_info.date)


def standarize_date(date_time):
    if len(date_time) <= 20:
        return date_time
    else:
        str_date = str(datetime.fromisoformat(date_time).astimezone(timezone.utc))[:19]
        date_time = str_date.replace(" ", "T") + "Z"
        return date_time

