import yfinance as yf
from technical_indicator.momentum import RSI


def fetch_stock_data(ticker, period='1mo'):
    '''
    Отвечает за загрузку данных об акциях
    :param ticker: Название акции
    :param period: период
    :return: Историю изменения цены закрытия
    '''
    stock = yf.Ticker(ticker)
    data = stock.history(period=period)
    return data


def add_moving_average(data, window_size=5):
    '''
    Добавляет в DataFrame колонку со скользящим средним, рассчитанным на основе цен закрытия.
    :param data: DataFrame
    :param window_size: Размер
    :return: изменённый DataFrame
    '''
    data['Moving_Average'] = data['Close'].rolling(window=window_size).mean()
    return data


def calculate_and_display_average_price(data):
    '''
    Вычисляет и выводит среднюю цену закрытия акций за заданный период.
    :param data: DataFrame
    :return:
    '''
    print(data['Close'].mean())


def notify_if_strong_fluctuations(data, threshold):
    '''
    Анализирует данные и уведомляет пользователя, если цена акций колебалась более чем на заданный процент за период.
    :param data: DataFrame
    :param threshold: Предел сравнения
    :return:
    '''
    if (data['Close'].max() - data['Close'].min()) > threshold:
        print('Значение больше порога!')
    else:
        return 0


def export_data_to_csv(data, filename):
    '''
    Cохраняет загруженные данные об акциях в CSV файл.
    :param data: DataFrame
    :param filename: имя файла
    :return: None
    '''
    data.to_csv(f'{filename}.csv')


def indicator_rsi(data, period=14):
    '''
    Расчёт RSI за указзанный период
    :param data: DataFrame
    :param period: Период RSI
    :return: значение RSI за указанный период
    '''
    rsi = RSI(list(data['Close']), period)
    return rsi.calculate_rsi()
