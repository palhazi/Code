from ibapi.client import EClient
from ibapi.common import Decimal, TickerId
from ibapi.utils import Decimal
from ibapi.wrapper import EWrapper
from ibapi.contract import Contract
from threading import Timer


class TestApp(EClient, EWrapper):
    def __init__(self):
        EClient.__init__(self, self)
        

    def error(self, reqId: TickerId, errorCode: int, errorString: str, advancedOrderRejectJson=""):
        print(reqId, errorCode, errorString, advancedOrderRejectJson)

    def nextValidId(self, orderId: int):
        self.start()

    def updatePortfolio(self, contract: Contract, position: Decimal, marketPrice: float, marketValue: float, averageCost: float, unrealizedPNL: float, realizedPNL: float, accountName: str):
        print(contract, position, marketPrice, marketValue, averageCost, unrealizedPNL, realizedPNL, accountName)

    def updateAccountValue(self, key: str, val: str, currency: str, accountName: str):
        print(key, val, currency, accountName)

    def updateAccountTime(self, timeStamp: str):
        print(timeStamp)

    def accountDownloadEnd(self, accountName: str):
        print(accountName)

    def start(self):
        self.reqAccountUpdates(True, "")

    def end(self):
        self.reqAccountUpdates(False, "")
        self.done = True
        self.disconnect()


app = TestApp()
app.connect("127.0.0.1", 4002, 0)
app.run()
