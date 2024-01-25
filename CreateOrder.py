from ibapi.client import EClient
from ibapi.wrapper import EWrapper
from ibapi.contract import Contract
import threading

class TradingApp(EClient, EWrapper):
    def __init__(self):
        EClient.__init__(self, wrapper=self)
        self.nextValidIdOrderId = None

    def error(self, reqId, errorCode, errorString, failError):
        print("Error: {} {} {}".format(reqId, errorCode, errorString, failError))

    def nextValidId(self, orderId):
        self.nextValidIdOrderId = orderId

app = TradingApp()
app.connect("127.0.0.1", 7497, 0)

t1 = threading.Thread(target=app.run)
t1.start()

while (app.nextValidIdOrderId == None):
    print("Waiting for TWS connection acknowledgement ...")

print("Connection established!")

# Define an Apple stock contract

c1 = Contract()

c1.symbol="AAPL"
c1.secType="STK"
c1.currency="USD"
c1.exchange="SMART"
c1.primaryExchange="NASDAQ"