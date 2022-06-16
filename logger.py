def log(text):
    f = open("log.txt", "a")
    f.write(f"{text}\n")
    f.close()
    print(text)