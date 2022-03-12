import random
import numpy as np
import matplotlib.pyplot as plt

# Функция треугольника
def function(x, n):
    if x < n:
        return 10 * x / n
    else:
        return 10 * ((x - 20) / (n - 20))

N = 200
n = 2
# Построение треугольника и вычисление его площади
def plottingTriangle(N, n):
    b = 10
    a = 20
    epsilon = 0.01

    # Массивы случайных точек
    xPoints = np.random.uniform(0, a, N)
    while(xPoints.mean() - a / 2 >= epsilon) or (xPoints.var() - a * a / 12 >= epsilon):
        xPoints = np.random.uniform(0, a, N)

    yPoints = np.random.uniform(0, b, N)
    while (yPoints.mean() - b / 2 >= epsilon) or (yPoints.var() - b * b / 12 >= epsilon):
        yPoints = np.random.uniform(0, b, N)

    # Массив x-ов
    x = np.arange(0, 20.1, step=0.5)

    # Вычисление значений функции
    y = np.array([])
    for i in range(len(x)):
        y = np.append(y, function(x[i], n))

    # Построение графика
    fig, ax = plt.subplots()
    ax.plot(x, y)

    # Вычисление количества случайных точек, лежащих внутри треугольника
    M = 0
    for i in range(N):
        if yPoints[i] < function(xPoints[i], n):
            M += 1
            # Построение точек
            plt.scatter(xPoints[i], yPoints[i], s=10, color='red')
        else:
            plt.scatter(xPoints[i], yPoints[i], s=10, color='black')

    # Приближённая площадь треугольника
    S = round(M / N * a * b, 2)
    print(f"Площадь фигуры: {S}")

    # Ещё точнее площадь
    S1 = 0
    for i in range(N):
        S1 += function(xPoints[i], n)
    S1 *= a / N
    S1 = round(S1, 4)
    print(f"Площадь фигуры: {S1}")

    ax.legend(fontsize=12,
              ncol=1,  # Количество столбцов
              facecolor='oldlace',  # Цвет области
              edgecolor='blue',  # Цвет крайней линии
              title=f'Всего генерируемых точек: {N} \n'
                    f'Точная площадь фигуры: 100 \n'
                    f'Площадь по Монте-Карло: {S1}',
              title_fontsize='12',  # Размер шрифта
              loc="upper right"
              )

    # Размер окна
    fig.set_figwidth(8)
    fig.set_figheight(8)

    # Удалить лишние пробелы
    fig.tight_layout()

    # Границы оси Y
    plt.ylim([0, 10])

    plt.show()

plottingTriangle(N, n)