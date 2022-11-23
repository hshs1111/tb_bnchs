#트레이딩 알고리즘
from coin_bot import CoinBot
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

bot = CoinBot()
client = bot.client
#코인 가격을 감시하고 거래실행

def get_price_history(client):
  klines = client.get_historical_klines('BNBBUSD', '1h', '9 day ago UTC', limit=1000)
  for line in klines:
    del line[5:]

  df = pd.DataFrame(klines, columns=['date', 'open', 'high', 'low', 'close'])
  df.set_index('date',inplace=True)
  df.index = pd.to_datetime(df.index, unit='ms')


  
  return df.astype(float)


# # def buy_coin_tp(client):
#   df = trade_based_on_crossover(client)                        
#   if buy_cross:
#     return client.order_market_buy(
#       symbol=symbol,
#       quantity=1.0,
#       price=str(buy_cross)
#     )
#   return None
# result = buy_coin_tp(client)
# print(result)

# def sell_coin_tp(self, symbol):
#   if sell_cross:
#     return client.order_market_sell(
#       symbol=symbol,
#       quantity=1.0,
#       price=str(sell_cross)
#     )
#   return None


    
# 1. 이동평균선보다 낮으면사고 높으면 팔기



def trade_based_on_5_sma(client):
  df = get_price_history(client)
                        
  df['5_sma'] = df['close'].rolling(5).mean()
  df['15_sma'] = df['close'].rolling(15).mean()
  
  # df['buy'] = np.where(df['5_sma'] > df['close'], 1, 0)
  # df['sell'] = np.where(df['5_sma'] <= df['close'], 1, 0)
  return df
  
print(get_price_history(client))


def trade_based_on_crossover(client):
  df = get_price_history(client)
                        
  df['5_sma'] = df['close'].rolling(5).mean()
  df['15_sma'] = df['close'].rolling(15).mean()

  df['signal'] = np.where(df['5_sma'] > df['15_sma'], 1, 0)
  df['position'] = df['signal'].diff()

  df['buy_cross'] = np.where(df['position'] == 1, df['5_sma'], np.NaN)
  df['sell_cross'] = np.where(df['position'] == -1, df['5_sma'], np.NaN)
  return df

print(trade_based_on_5_sma(client))
def plot_crossover_graph(client):
  df = trade_based_on_crossover(client)
  df[['5_sma', '15_sma']].plot()

  plt.scatter(df.index, df['buy_cross'], color='red', label='Buy', marker='^', alpha=1)
  plt.scatter(df.index, df['sell_cross'], color='blue', label='Sell', marker='v', alpha=1)
  
  plt.xlabel('Data')
  plt.ylabel('Pirce')
  # plt.show()
# plot_crossover_graph(client)
