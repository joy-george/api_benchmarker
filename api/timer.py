import datetime
from app_utils import execution_time
from dateutil.tz import tzlocal

@execution_time.calculate
def get_current_time():
    response = {"currentDateTime": datetime.datetime.now(tzlocal()).strftime('%Y-%m-%d %H:%M:%S %Z')}
    return response
