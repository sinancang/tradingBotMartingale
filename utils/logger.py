import datetime

def log(text):
    datetime_now = datetime.datetime.now().strftime("[%Y/%m/%d -- %H:%M:%S]")
    date_now = datetime.date.today().strftime("%Y%m%d")
    f = open(f"{date_now}.log.txt", "a")
    f.write(f"{datetime_now} : {text}\n")
    f.close()
    print(text)