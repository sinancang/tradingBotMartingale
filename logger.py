import datetime

def log(text):
    f = open("log.txt", "a")
    date_now = datetime.datetime.now().strftime("[%d/%m/%Y -- %H:%M:%S]")
    f.write(f"{date_now} -- {text}\n")
    f.close()
    print(text)