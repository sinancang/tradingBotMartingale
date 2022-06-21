from logger import log

import os
from websocket import create_connection

# need to create a message object instead of sending these messages inside method
class recorder():
    def __init__(self, ws):
        self.ws = ws

    def logon(self):
        log("Logging in...")
        logon = {"action": "auth", "key": os.environ['APCA_API_KEY_ID'], "secret": os.environ['APCA_API_SECRET_KEY']}
        self.ws.send(logon)
        log(f">{logon}")

        result = self.ws.recv()
        log(f"<{result}")

        # should return 1 if auth failed
        return 0

    # might want to take in some parameters
    def subscribe(self):
        print("Not implemented yet")

def connect():
    log("Connecting...")
    ws = create_connection("wss://stream.data.alpaca.markets/v2/iex")
    result = ws.recv()
    log(f"<{result}")

    # need to return None if connection fails
    # will take care of it once I figure out the parsing
    return ws

# connection and logging seem to work, will try out subscription this monday
# lastly, need to figure out a consistent data storage format...
def main():
    ws = connect()
    rc = recorder(ws)
    rc.subscribe()


if __name__ == "__main__":
    main()