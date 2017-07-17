import datetime

def past_unix_timestamp_from_now(days = 1):
    day = datetime.date.today() - datetime.timedelta(days)
    unix_timestamp = day.strftime("%s")
    return unix_timestamp
