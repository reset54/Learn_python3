import datetime
import pytz

timezone = pytz.timezone("Europe/Moscow")
now = timezone.localize(datetime.datetime.now())

# append row in file "now.txt"
with open("./now.txt", "a") as f:
    f.write(f"Now: {now.hour:02d}:{now.minute:02d}:{now.second:02d}\n")