from pprint import pprint

import matplotlib.pyplot as plt

import data_download as dd
import data_plotting as dplt


def main():
    print("Добро пожаловать в инструмент получения и построения графиков биржевых данных.")
    print(
        "Вот несколько примеров биржевых тикеров, которые вы можете рассмотреть: AAPL (Apple Inc), GOOGL (Alphabet Inc), MSFT (Microsoft Corporation), AMZN (Amazon.com Inc), TSLA (Tesla Inc).")
    print(
        "Общие периоды времени для данных о запасах включают: 1д, 5д, 1мес, 3мес, 6мес, 1г, 2г, 5г, 10л, с начала года, макс.")

    ticker = input("Введите тикер акции (например, «AAPL» для Apple Inc):»")
    period = input(
        "Введите период для данных (например, '1mo' для одного месяца или период начала измерения и оканчание 'YYYY-MM-DD YYYY-MM-DD'): ")
    threshold = int(input('Введите порог превышения разницы цены закрытия: '))
    file_name_csv = input('Введите имя файла для сохранения данных в формате CSV: ')
    pprint(plt.style.available)
    style = input('Введите стиль графика: ')
    # Fetch stock data
    stock_data = dd.fetch_stock_data(ticker, period)

    # Add moving average to the data
    stock_data = dd.add_moving_average(stock_data)
    # Plot the data
    dplt.create_and_save_plot(stock_data, ticker, period, style_name=style)
    dd.calculate_and_display_average_price(stock_data)
    dd.notify_if_strong_fluctuations(stock_data, threshold)
    dd.export_data_to_csv(stock_data, file_name_csv)
    dd.average_price_close(stock_data)


if __name__ == "__main__":
    main()
