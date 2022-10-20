#트레이딩 알고리즘
from coin_bot import CoinBot
import time

bot = CoinBot()
client = bot.client
#코인 가격을 감시하고 거래실행

def buy_coin_tp(self, symbol, t_price):
  ticker_info = self.client.get_ticker(symbol=symbol)
  last_price = ticker_info['lastPrice'] 
  last_price = round(float(last_price), 2)
  if last_price <= t_price:
    return client.order_market_buy(
      symbol=symbol,
      quantity=1.0,
      price=str(t_price)
    )
  return None


def sell_coin_tp(self, symbol, t_price):
  ticker_info = self.client.get_ticker(symbol=symbol)
  last_price = ticker_info['lastPrice'] 
  last_price = round(float(last_price), 2)
  if last_price <= t_price:
    return client.order_market_buy(
      symbol=symbol,
      quantity=1.0,
      price=str(t_price)
    )
  return None


while True:
  time.sleep(3600)
  buy_coin_tp(client, 'BTCUSDT', 19200)
  sell_coin_tp(client, 'BTCUSDT', 20000)
    


