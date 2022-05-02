import datetime
import re

TEE_TIME = '1:00 PM'


today = datetime.date.today()
date_of_round = today + datetime.timedelta(days=7)
day = datetime.datetime.strptime(str(date_of_round), "%Y-%m-%d")
dow = day.day
print(dow)


def get_correct_tee_time(TEE_TIME):
    time = TEE_TIME
    hr = time.split(":")
    mins = hr[1].split(" ")
    hour, minutes, tod = hr[0], mins[0], mins[1]
    return hour, minutes, tod

H, M, ToD = get_correct_tee_time(TEE_TIME)

print(H)
print(M)
print(ToD)