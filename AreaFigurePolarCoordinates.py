import math
import random
import numpy as np
import matplotlib.pyplot as plt

A = 17
B = 7

def po(ph, A, B):
    return math.sqrt(A * pow(np.cos(ph), 2) + B * pow(np.sin(ph), 2))

def curPh(x, y):
    if x > 0:
        return np.arctan(y / x)
    elif x < 0:
        return np.pi + np.arctan(y / x)
    elif x == 0 and y > 0:
        return np.pi / 2
    elif x == 0 and y < 0:
        return np.pi * 3 / 2
    elif x == 0 and y == 0:
        return 0
    else:
        return "Офыбка"

def plotting(A, B):
    N = 1000

    fig, ax = plt.subplots()

    ph = np.linspace(0, 2 * np.pi, num=300)

    x = np.array([])
    y = np.array([])
    for i in range(len(ph)):
        x = np.append(x, po(ph[i], A, B) * np.cos(ph[i]))
        y = np.append(y, po(ph[i], A, B) * np.sin(ph[i]))

    ax.plot(x, y)

    a = max(x)
    b = max(y)

    # Генерация массивов случайных точек
    xPoints = np.random.uniform(0, 2 * a, N) - a
    yPoints = np.random.uniform(0, 2 * b, N) - b

    M = 0
    for i in range(N):
        if (math.sqrt(pow(xPoints[i], 2) + pow(yPoints[i], 2))) < po(curPh(xPoints[i], yPoints[i]), A, B):
            plt.scatter(xPoints[i], yPoints[i], s=10, color='red')
            M += 1
        else:
            plt.scatter(xPoints[i], yPoints[i], s=10, color='black')

    S = M / N * (a * b * 4)
    print(f'Площадь фигуры: {S}')

    ax.legend(fontsize=12,
              ncol=1,  # Количество столбцов
              facecolor='oldlace',  # Цвет области
              edgecolor='blue',  # Цвет крайней линии
              title=f'Кол-во генерируемых точек: {N} \n'
                    f'Площадь вручную: 37.843 \n'
                    f'Площадь по Монте-Карло: {S}',
              title_fontsize='13',  # Размер шрифта
              loc="upper left"
              )

    # Размер окна
    fig.set_figwidth(8)
    fig.set_figheight(8)

    # Удалить лишние пробелы
    fig.tight_layout()

    # Границы оси Y и X
    plt.ylim([min(y), max(y)])
    plt.xlim([min(x), max(x)])

    plt.show()

plotting(A, B)