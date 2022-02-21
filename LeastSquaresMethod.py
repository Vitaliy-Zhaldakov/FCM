import math
import matplotlib.pyplot as plt
import numpy as np
#import wx

# Нахождение решения системы уравнений
def systemSolution(inputMatrix):

    # Сумма по "x"
    sumX = 0
    for x in range(len(inputMatrix)):
        sumX += inputMatrix[x, 0]

    # Сумма по "y"
    sumY = 0
    for y in range(len(inputMatrix)):
        sumY += inputMatrix[y, 1]

    # Сумма по "x^2"
    sumX2 = 0
    for x in range(len(inputMatrix)):
        sumX2 += pow(inputMatrix[x, 0], 2)

    # Сумма по "x * y"
    sumXY = 0
    for elem in range(len(inputMatrix)):
        sumXY += inputMatrix[elem, 0] * inputMatrix[elem, 1]

    # Коэффициенты системы уравнения
    coeffMatrix = np.array([[sumX2, sumX], [sumX, len(inputMatrix)]])
    # Вектор свободных членов
    vector = np.array([sumXY, sumY])

    # Решение системы уравнений
    solution = np.linalg.solve(coeffMatrix, vector)
    return solution

# Поиск зависимости "y" от "x" в виде линейной функции y = ax + b
def linearFunction(inputMatrix):

    # Решение системы
    return np.around(systemSolution(inputMatrix), 2)

# Поиск зависимости "y" от "x" в виде степенной функции y = b * x^a
def powerFunction(inputMatrix):

    # Прологарифмируем функцию и получим зависимости X = ln(x) и Y = ln(y)
    logMatrix = inputMatrix.copy()
    for elem in logMatrix:
        elem[0] = math.log(elem[0])
        elem[1] = math.log(elem[1])

    # Решение системы
    solution = np.around(systemSolution(logMatrix), 2)[::-1]

    # Учитывая, что B = ln(b), находим b = e^B
    solution[0] = math.exp(solution[0]).__round__(2)
    return solution


# Поиск зависимости "y" от "x" в виде показательной функции y = B * e^(ax)
def exponentialFunction(inputMatrix):

    # Прологарифмируем функцию и получим зависимости x = x и Y = ln(y)
    logMatrix = inputMatrix.copy()
    for y in logMatrix:
        y[1] = math.log(y[1])

    # Решение системы
    solution = np.around(systemSolution(logMatrix), 2)[::-1]

    # Учитывая, что B = ln(b), находим b = e^B
    solution[0] = math.exp(solution[0]).__round__(2)
    return solution

# Поиск зависимости "y" от "x" в виде квадратичной функции y = ax^2 + bx + c
def quadraticFunction(inputMatrix):

    # Cумма по "x"
    sumX = 0
    for x in range(len(inputMatrix)):
        sumX += inputMatrix[x, 0]

    # Cумма по "x^2"
    sumX2 = 0
    for x in range(len(inputMatrix)):
        sumX2 += pow(inputMatrix[x, 0], 2)

    # Cумма по "x^3"
    sumX3 = 0
    for x in range(len(inputMatrix)):
        sumX3 += pow(inputMatrix[x, 0], 3)

    # Cумма по "x^4"
    sumX4 = 0
    for x in range(len(inputMatrix)):
        sumX4 += pow(inputMatrix[x, 0], 4)

    # Cумма по "y"
    sumY = 0
    for y in range(len(inputMatrix)):
        sumY += inputMatrix[y, 1]

    # Cумма по "x * y"
    sumXY = 0
    for elem in range(len(inputMatrix)):
        sumXY += inputMatrix[elem, 0] * inputMatrix[elem, 1]

    # Cумма по "x^2 * y"
    sumX2Y = 0
    for elem in range(len(inputMatrix)):
        sumX2Y += pow(inputMatrix[elem, 0], 2) * inputMatrix[elem, 1]

    # Матрица коэффициентов
    coeffMatrix = np.array([[sumX4, sumX3, sumX2], [sumX3, sumX2, sumX],
                   [sumX2, sumX, len(inputMatrix)]])

    # Вектор свободных членов
    vector = np.array([sumX2Y, sumXY, sumY])

    # Решение системы
    solution = np.linalg.solve(coeffMatrix, vector)

    return np.around(solution, 2)

# Построение графиков полученных функций с нанесением экспериментальных точек
def PlottingFunctions(inputMatrix):

    # Точки построения графика
    x = np.linspace(inputMatrix[0, 0] - 1, inputMatrix[-1, 0] + 1, num=100)

    linear = linearFunction(inputMatrix)
    power = powerFunction(inputMatrix)
    exponential = exponentialFunction(inputMatrix)
    quadratic = quadraticFunction(inputMatrix)

    linY = linear[0] * x + linear[1]
    powerY = power[0] * np.power(x, power[1])
    expY = exponential[0] * np.exp(x * exponential[1])
    quadY = (quadratic[0] * x * x) + (quadratic[1] * x) + quadratic[2]

    fig, ax = plt.subplots()

    ax.plot(x, linY, label=f'y = {linear[0]}*x + {linear[1]}')
    ax.plot(x, powerY, label=f'y = {power[0]}*x^{power[1]}')
    ax.plot(x, expY, label=f'y = {exponential[0]}*exp^(x*{exponential[1]})')
    ax.plot(x, quadY, label=f'y = ({quadratic[0]}*x^2) + ({quadratic[1]}*x) + ({quadratic[2]}) ')

    ax.legend(fontsize=12,
              ncol=1,  # Количество столбцов
              facecolor='oldlace',  # Цвет области
              edgecolor='blue',  # Цвет крайней линии
              title='Графики функций',  # Заголовок
              title_fontsize='20',  # Размер шрифта
              loc="upper left"
              )

    fig.set_figwidth(12)
    fig.set_figheight(12)

    for elem in range(len(inputMatrix)):
        # scatter - метод для нанесения маркера в точке
        plt.scatter(inputMatrix[elem, 0], inputMatrix[elem, 1], s=20, color='black')

    inacLinear = 0
    inacPower = 0
    inacExp = 0
    inacQuad = 0

    # Вычисление погрешностей
    for elem in range(len(inputMatrix)):
        inacLinear += round(pow(inputMatrix[elem, 1] - (linear[0] * inputMatrix[elem, 0] + linear[1]), 2), 2)
        inacPower += round(pow(inputMatrix[elem, 1] - (power[0] * pow(inputMatrix[elem, 0], power[1])), 2), 2)
        inacExp += round(pow(inputMatrix[elem, 1] - (exponential[0] * math.exp(inputMatrix[elem, 0] * exponential[1])), 2), 2)
        inacQuad += round(
        pow(inputMatrix[elem, 1] - ((quadratic[0] * inputMatrix[elem, 0] * inputMatrix[elem, 0]) + (quadratic[1] * inputMatrix[elem, 0]) + quadratic[2]), 2), 2)

    if (inacLinear == min(inacQuad, inacLinear, inacExp, inacPower)):
        print("В данной задаче лучшей аппроксимирующей функцией является линейная функция")
    elif (inacPower == min(inacQuad, inacLinear, inacExp, inacPower)):
        print("В данной задаче лучшей аппроксимирующей функцией является степенная функция")
    elif (inacExp == min(inacQuad, inacLinear, inacExp, inacPower)):
        print("В данной задаче лучшей аппроксимирующей функцией является показательная функция")
    else:
        print("В данной задаче лучшей аппроксимирующей функцией является квадратичная функция")

    print(f"Погрешность линейной функции: {inacLinear}")
    print(f"Погрешность степенной функции: {inacPower}")
    print(f"Погрешность показательной функции: {inacExp}")
    print(f"Погрешность квадратичной функции: {inacQuad}")

    plt.show()

inputMatrix = np.array([[1, 1], [2, 1.5], [3, 3], [4, 4.5], [5, 7], [6, 8.5]])
PlottingFunctions(inputMatrix)



