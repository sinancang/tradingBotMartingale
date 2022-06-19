from logger import log

import os
from websocket import create_connection

# need to figure out a way to continually recieve and send messages: might want to create a separate connection class
# also need to log every message sent and every message received
# nevertheless the connection and logging seem to work, will try out subscription this monday
# lastly, need to figure out a consistent data storage format...
def main():
    log("Connecting...")
    ws = create_connection("wss://stream.data.alpaca.markets/v2/iex")
    result = ws.recv()
    log(result)

    log("Logging in...")
    #logon = {"action": "auth", "key": os.environ['APCA_API_KEY_ID'], "secret": os.environ['APCA_API_SECRET_KEY']}
    logon = '{"action": "auth", "key": "PKE6Z2F0ZB01FQJDI057", "secret": "OJvJ8tmMkp56jbFo06TyouAbJdGqsKkt85w28XJe"}'
    ws.send(logon)
    result = ws.recv()
    log(result)

    subscription = '{"action":"subscribe","trades":["AAPL"],"quotes":["AMD","CLDR"],"bars":["AAPL","VOO"]}'
    ws.send(subscription)
    result = ws.recv()
    log(result)

    result = ws.recv()
    log(result)

    ws.close()

if __name__ == "__main__":
    main()