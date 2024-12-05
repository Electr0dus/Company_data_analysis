import yfinance as yf


def fetch_stock_data(ticker, period='1mo'):
    stock = yf.Ticker(ticker)
    data = stock.history(period=period)
    return data


def add_moving_average(data, window_size=5):
    data['Moving_Average'] = data['Close'].rolling(window=window_size).mean()
    return data


def calculate_and_display_average_price(data):
    print(data['Close'].mean())

def notify_if_strong_fluctuations(data, threshold):
    if (data['Close'].max() - data['Close'].min()) > threshold:
        print('Значение больше порога!')
    else:
        return 0
