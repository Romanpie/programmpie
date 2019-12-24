# Коды из справочника
# 2203, Пиво
# 2208 Спиртные напитки
# 2204, ВИНА ВИНОГРАДНЫЕ НАТУРАЛЬНЫЕ

import csv
import matplotlib.pyplot as plt
import pandas as pd

beer = {}
wine = {}
alcohol = {}
all = {}
# Все словари вида {страна : количество}


with open('TCBT.csv', newline='', errors='replace') as csvfile:
    reader = csv.reader(csvfile, quotechar=',')
    for row in reader:
        if row[3] == '2203':
            beer[row[2]] = beer.setdefault(row[2], 0) + int(str(row[8]).split(' ')[0])
            all[row[2]] = all.setdefault(row[2], 0) + int(str(row[8]).split(' ')[0])
        elif row[3] == '2204':
            wine[row[2]] = wine.setdefault(row[2], 0) + int(str(row[8]).split(' ')[0])
            all[row[2]] = all.setdefault(row[2], 0) + int(str(row[8]).split(' ')[0])
        elif row[3] == '2208':
            alcohol[row[2]] = alcohol.setdefault(row[2], 0) + int(str(row[8]).split(' ')[0])
            all[row[2]] = all.setdefault(row[2], 0) + int(str(row[8]).split(' ')[0])

# Берём словарь с пивом, создаём dataframe из пар страна - количество
beer_df = pd.DataFrame(list(beer.items()), columns=['Country_Name', 'Amount'])
beer_df = beer_df.sort_values(by=['Amount'], ascending=False)
beer_df = beer_df[0:10]

wine_df = pd.DataFrame(list(wine.items()), columns=['Country_Name', 'Amount'])
wine_df = wine_df.sort_values(by=['Amount'], ascending=False)
wine_df = wine_df[0:10]

alcohol_df = pd.DataFrame(list(alcohol.items()), columns=['Country_Name', 'Amount'])
alcohol_df = alcohol_df.sort_values(by=['Amount'], ascending=False)
alcohol_df = alcohol_df[0:10]

all_df = pd.DataFrame(list(all.items()), columns=['Country_Name', 'Amount'])
all_df = all_df.sort_values(by=['Amount'], ascending=False)
all_df = all_df[0:10]

plt.style.use('seaborn-deep')
plt.rcParams['font.family'] = 'Tahoma'


# Функция для визуализации данных, на вход подаётся список пар и название графика
def visualize_results(df, name):
    nam, val = list(df['Country_Name']), list(df['Amount'])
    fig, ax = plt.subplots()
    for i in range(len(df)):
        ax.bar(nam[i], val[i])
        ax.text(nam[i], val[i] + val[i] / 100, "{}\nтыс. штук".format(str(val[i] // 1000)),
                horizontalalignment='center', color='#949cab')  # Подписываем этот столбик его значением
    ax.set(ylim=(min(val) - min(val) / 10, max(val) + max(val) / 10))  # Задаём верхнюю и нижнюю границу графика
    ax.axes.get_yaxis().set_visible(False)  # Выключаем отображение оси У(столбики уже подписаны)
    ax.grid(False)  # Выключаем сетку, в ней нет необходимости
    ax.set_facecolor('#36393f')  # Задаём цвет фона
    ax.tick_params(axis='both', which='major', labelsize=14)  # Задаём размер подписей снизу
    plt.setp(ax.spines.values(), color="#ffffff")  # Задаём цвет всех шкал
    ax.tick_params(axis='x', colors='#747c89')  # Задаём цвет шкалы Х
    fig.set_figwidth(12)  # Задаём ширину графика
    fig.set_figheight(6)  # Задаём высоту графика
    plt.gcf().set_facecolor('#2f3136')  # Задаём цвет вне графика
    plt.title(name, color='#c4cfe0', fontsize=16)  # Задаём текст, цвет и размер названия
    plt.savefig(name + '.png', transparent=True)
    plt.show()  # Выводим график на экран


visualize_results(beer_df, "Топ-{} стран по объёмам поставки пива".format(len(beer_df)))
visualize_results(wine_df, "Топ-{} стран по объёмам поставки вина".format(len(wine_df)))
visualize_results(alcohol_df, "Топ-{} стран по объёмам поставки спиртосодержащих напитков".format(len(alcohol_df)))
visualize_results(all_df, "Топ-{} стран по объёмам поставки алкогольных напитков всех видов".format(len(alcohol_df)))