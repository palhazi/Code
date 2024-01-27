from ibapi.client import *
from ibapi.wrapper import *


class TestApp(EClient, EWrapper):
    def __init__(self):
        EClient.__init__(self, self)
        

    def nextValidId(self, orderId: int):
        
        mycontract = Contract()
        mycontract.symbol = "AAPL"
        mycontract.secIdType = "STK"
        mycontract.exchange = "SMART"
        mycontract.currency = "USD"



app = TestApp()
app.connect("127.0.0.1", 4002, 0)
app.run()


