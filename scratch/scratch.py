import datetime
from config.secrets import TEE_TIME


today = datetime.date.today()
date_of_round = today + datetime.timedelta(days=7)
day = datetime.datetime.strptime(str(date_of_round), "%Y-%m-%d")
dow = day.day
print(dow)


def get_tee_time_ready():
    hr = TEE_TIME
    print(hr)



# hr, mins, tod = get_tee_time_ready(TEE_TIME)
get_tee_time_ready(TEE_TIME)