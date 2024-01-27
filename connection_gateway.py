from ibapi.client import *
from ibapi.common import TickAttrib, TickerId
from ibapi.ticktype import TickType
from ibapi.wrapper import *


class TestApp(EClient, EWrapper):
    def __init__(self):
        EClient.__init__(self, self)
        

    def nextValidId(self, orderId: int):
        
        mycontract = Contract()
        mycontract.symbol = "AAPL"
        mycontract.secType = "STK"
        mycontract.exchange = "SMART"
        mycontract.currency = "USD"

        self.reqMarketDataType(4)
        self.reqMktData(orderId, mycontract, "", 0, 0, [])

    def tickPrice(self, reqId, TickType, price, attrib):
        print(f"tickPrice. reqId: {reqId}, tickType: {TickTypeEnum.to_str(TickType)}, price: {price}, attribs: {attrib}")
        
    def tickSize(self, reqId, TickType, size):
        print(f"ticksize. reqId: {reqId}, tickType: {TickTypeEnum.to_str(TickType)}, size: {size}")


app = TestApp()
app.connect("127.0.0.1", 4002, 0)
app.run()


