import math
import random
import numpy as np
import matplotlib.pyplot as plt

R = 2
N = 200
def plotting(N, R):
    e = 0.01

    # Генерация массивов случайных точек
    xPoints = np.random.uniform(0, R * 2, N)
    while (xPoints.mean() - R * 2 / 2 >= e) or (xPoints.var() - R * 2 * R * 2 / 12 >= e):
        xPoints = np.random.uniform(0, R * 2, N)

    yPoints = np.random.uniform(0, R * 2, N)
    while (yPoints.mean() - R * 2 / 2 >= e) or (yPoints.var() - R * 2 * R * 2 / 12 >= e):
        yPoints = np.random.uniform(0, R * 2, N)

    fig, ax = plt.subplots()

    ph = np.linspace(0, 2 * np.pi, num=150)

    # Вычисление точек окружности, заданной параметрически
    x = np.array([])
    y = np.array([])
    for i in range(len(ph)):
        x = np.append(x, R + R * np.cos(ph[i]))
        y = np.append(y, R + R * np.sin(ph[i]))

    ax.plot(x, y)

    # Выделение точек, расположенных внутри окружности
    M = 0
    for j in range(N):
        if math.pow(xPoints[j] - R, 2) + math.pow(yPoints[j] - R, 2) < R * R:
            plt.scatter(xPoints[j], yPoints[j], s=10, color='red')
            M += 1
        else:
            plt.scatter(xPoints[j], yPoints[j], s=10, color='black')

    S = M / N * pow((2 * R), 2)
    print(f"Площадь фигуры: {S}")

    # Вычисление числа Pi
    pi = S / pow(R, 2)

    ax.legend(fontsize=12,
              ncol=1,  # Количество столбцов
              facecolor='oldlace',  # Цвет области
              edgecolor='blue',  # Цвет крайней линии
              title=f'Кол-во генерируемых точек: {N} \n'
                    f'Pi = {pi}',
              title_fontsize='13',  # Размер шрифта
              loc="upper left"
              )

    # Размер окна
    fig.set_figwidth(8)
    fig.set_figheight(8)

    # Удалить лишние пробелы
    fig.tight_layout()

    # Границы оси Y и X
    plt.ylim([0, R * 2])
    plt.xlim([0, R * 2])

    plt.show()

plotting(N, R)