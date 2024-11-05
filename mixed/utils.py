import time
from datetime import datetime


def now() -> str:
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())


def get_current_date() -> str:
    return time.strftime("%Y-%m-%d", time.localtime())


def date_format(date, input_format="%Y-%m-%d", output_format="%Y-%m-%d"):
    date_obj = datetime.strptime(date, input_format)
    return date_obj.strftime(output_format)


curdate = get_current_date
