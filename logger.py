def log(text):
    f = open("log.txt", "a")
    f.write(text)
    f.close()
    print(text)