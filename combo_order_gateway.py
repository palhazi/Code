from ibapi.client import *
from ibapi.common import Decimal, OrderId
from ibapi.contract import Contract, ContractDetails, ComboLeg
from ibapi.execution import Execution
from ibapi.order import Order
from ibapi.order_state import OrderState
from ibapi.utils import Decimal
from ibapi.wrapper import *
from ibapi.tag_value import TagValue


class TestApp(EClient, EWrapper):
    def __init__(self):
        EClient.__init__(self, self)
        

    def nextValidId(self, orderId: int):
        
        mycontract = Contract()
        mycontract.symbol = "AAPL,TSLA"
        mycontract.secType = "BAG"
        mycontract.exchange = "SMART"
        mycontract.currency = "USD"

        leg1 = ComboLeg()
        leg1.conId = 76792991
        leg1.ratio = 1
        leg1.action = "BUY"
        leg1.exchange = "SMART"

        leg2 = ComboLeg()
        leg2.conId = 265598
        leg2.ratio = 1
        leg2.action = "SELL"
        leg2.exchange = "SMART"

        mycontract.comboLegs = []
        mycontract.comboLegs.append(leg1)
        mycontract.comboLegs.append(leg2)

        myorder = Order()
        myorder.orderId = orderId
        myorder.action = "BUY"
        myorder.orderType = "LMT"
        myorder.lmtPrice = 80
        myorder.totalQuantity = 10
        myorder.tif = "GTC"
        myorder.smartComboRoutingParams = []
        myorder.smartComboRoutingParams.append(TagValue('NonGuaranteed', '1'))

        self.placeOrder(OrderId, mycontract, myorder)



    def openOrder(self, orderId: OrderId, contract: Contract, order: Order, orderState: OrderState):
        print(f"openOrder. orderId: {orderId}, contract: {contract}, order: {order}")


    def orderStatus(self, orderId: OrderId, status: str, filled: Decimal, remaining: Decimal, avgFillPrice: float, permId: int, parentId: int, lastFillPrice: float, clientId: int, whyHeld: str, mktCapPrice: float):
        print(f"orderStatus.orderId: {orderId}, status: {status}, filled: {filled}, remaining: {remaining}, avgFillprice: {avgFillPrice}, permId: {permId}")
    

    def execDetails(self, reqId: int, contract: Contract, execution: Execution):
        print(f"execDetails.reqId: {reqId}, contract: {contract}, execution: {execution}")
      
  


app = TestApp()
app.connect("127.0.0.1", 4002, 0)
app.run()