from ibapi.client import EClient
from ibapi.wrapper import EWrapper
from ibapi.contract import Contract
from ibapi.order import Order
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

# Define an Apple stock contract ---- https://interactivebrokers.github.io/tws-api/

c1 = Contract()

c1.symbol="AAPL"
c1.secType="STK"
c1.currency="USD"
c1.exchange="SMART"
c1.primaryExchange="NASDAQ"

orderId = app.nextValidIdOrderId

# Create entry order

entryOrder = Order()

entryOrder.orderId = orderId
entryOrder.action = "BUY"
entryOrder.orderType = "LMT"
entryOrder.totalQuantity = 10
entryOrder.lmtPrice = 190
entryOrder.transmit = False

# Create profit order

profitOrder = Order()

profitOrder.orderId = orderId + 1
profitOrder.parentId = entryOrder.orderId
profitOrder.action = "SELL"
profitOrder.orderType = "LMT"
profitOrder.totalQuantity = 10
profitOrder.lmtPrice = 200
profitOrder.transmit = False

# Create STOP-LOSS order

stopLossOrder = Order()

stopLossOrder.orderId = orderId + 2
stopLossOrder.parentId = entryOrder.orderId
stopLossOrder.action = "SELL"
stopLossOrder.orderType = "LMT"
stopLossOrder.totalQuantity = 10
stopLossOrder.auxPrice = 180
stopLossOrder.transmit = True

# Place order

app.placeOrder (orderId, c1, entryOrder)
orderId+=1
app.placeOrder (orderId, c1, profitOrder)
orderId+=1
app.placeOrder (orderId, c1, stopLossOrder)
orderId+=1