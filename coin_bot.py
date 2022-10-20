from binance.client import Client

class CoinBot:
  API_KEY = 'bssW4Xpf2nTPtEDVWHkrDkmO5JBXqYlrKMmUOTlCvwCUQdMLzWuhTkblTGEv8xJ9'
  API_SECRET = 'hcGXWdDnIMYBLy6FoPzKO58GdBzalFY1lpmK2hizfBihWX2xdbBPYUD6qdk4Vm4K'
  
  def __init__(self):
    self.client = Client(self.API_KEY, self.API_SECRET, testnet=True)

    
  def buy_coin_dc(self, symbol, quantity):
  # 1.코인의 현재가
    ticker_info = self.client.get_ticker(symbol=symbol)
    last_price = ticker_info['lastPrice'] #현재가
    #print(last_price) #출력
  
  # 2.코인의 현재가에서 5퍼빠진가격
    dc_price = round(float(last_price) * 0.95, 2)
  
  # 3.정해진가격에 주문넣기
    order = self.client.order_limit_buy(
      symbol=symbol,
      quantity=quantity,
      price=str(dc_price)
    )

    return order

    # 4. 시장가 구매,판매
  def buy_coin_amp(self, symbol, quantity):
    order = self.client.order_market_buy(
       symbol=symbol,
       quantity=quantity,
      
    )
    return order

   #5.체결주문 취소
  def cancel_all(self):
    open_order = self.client.get_open_orders()
    for order in open_order:
      result = self.client.cancel_order(
        symbol=order['symbol'],
        orederid=order['orderid']
      )
      print(result)
    

# print(client.get_account())
bot = CoinBot()
account_info = bot.client.get_account()
print(account_info)
# order_result = bot.buy_coin_amp('LTCUSDT',50)
# print(order_result)