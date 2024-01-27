from ibapi.client import *
from ibapi.common import Decimal, OrderId
from ibapi.contract import Contract, ContractDetails
from ibapi.execution import Execution
from ibapi.order import Order
from ibapi.order_state import OrderState
from ibapi.utils import Decimal
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

        self.reqContractDetails(orderId, mycontract)

    def contractDetails(self, reqId: int, contractDetails: ContractDetails):
        print(contractDetails.contract)

        myorder = Order()
        myorder.orderId = reqId
        myorder.action = "BUY"
        myorder.tif = "GTC"
        myorder.orderType = "MKT"
        myorder.totalQuantity = 10

        self.placeOrder(reqId, contractDetails.contract, myorder)

    def openOrder(self, orderId: OrderId, contract: Contract, order: Order, orderState: OrderState):
        print(f"openOrder. orderId: {orderId}, contract: {contract}, order: {order}")


    def orderStatus(self, orderId: OrderId, status: str, filled: Decimal, remaining: Decimal, avgFillPrice: float, permId: int, parentId: int, lastFillPrice: float, clientId: int, whyHeld: str, mktCapPrice: float):
        print(f"orderStatus.orderId: {orderId}, status: {status}, filled: {filled}, remaining: {remaining}, avgFillprice: {avgFillPrice}, permId: {permId}")
    

    def execDetails(self, reqId: int, contract: Contract, execution: Execution):
        print(f"execDetails.reqId: {reqId}, contract: {contract}, execution: {execution}")
      





    


app = TestApp()
app.connect("127.0.0.1", 4002, 0)
app.run()