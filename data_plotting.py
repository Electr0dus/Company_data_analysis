import matplotlib.pyplot as plt
import pandas as pd
import data_download as dd


def create_and_save_plot(data, ticker, period, style_name, filename=None):
    '''
    Создаёт график, отображающий цены закрытия и скользящие средние. Предоставляет возможность сохранения графика в файл.
    Параметр filename опционален; если он не указан, имя файла генерируется автоматически.
    :param style_name: Стиль рисования графика
    :param data: DataFrame
    :param ticker: Акция
    :param period: Период определения
    :param filename: Имя файла
    :return:
    '''
    plt.figure(figsize=(10, 6))
    plt.style.use(style_name)
    if 'Date' not in data:
        if pd.api.types.is_datetime64_any_dtype(data.index):
            dates = data.index.to_numpy()
            plt.plot(dates, data['Close'].values, label='Close Price')
            plt.plot(dates, data['Moving_Average'].values, label='Moving Average')
        else:
            print("Информация о дате отсутствует или не имеет распознаваемого формата.")
            return
    else:
        if not pd.api.types.is_datetime64_any_dtype(data['Date']):
            data['Date'] = pd.to_datetime(data['Date'])
        plt.plot(data['Date'], data['Close'], label='Close Price')
        plt.plot(data['Date'], data['Moving_Average'], label='Moving Average')

    plt.title(f"{ticker} Цена акций с течением времени")

    plt.text(x=0, y=0.9, s=f'RSI = {dd.indicator_rsi(data):.2f} за 14 дней', fontsize=15, color='green',
             transform=plt.gca().transAxes)
    plt.text(x=0, y=0.8, s=f'STDev = {dd.indicator_standart_devation_closing(data):.2f}', fontsize=15, color='blue',
             transform=plt.gca().transAxes)
    plt.xlabel("Дата")
    plt.ylabel("Цена")
    plt.legend()

    if filename is None:
        filename = f"{ticker}_{period}_stock_price_chart.png"

    plt.savefig(filename)
    print(f"График сохранен как {filename}")


print(plt.style.available)