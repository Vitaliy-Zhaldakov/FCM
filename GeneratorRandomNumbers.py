import matplotlib.pyplot as plt
import numpy as np

# Метод квадратов
def methodSquares(num, iter, array):
    lengthNum = len(num)

    for i in range(iter):
        squareNum = str(pow(int(num), 2))

        while len(squareNum) != lengthNum * 2:
            squareNum = "0" + squareNum

        # Список средних разрядов
        new = squareNum[int(lengthNum - lengthNum/2) : int(lengthNum + lengthNum/2)]

        # Преобразование в новое число в интервале (0; 1)
        # Добавление числа в массив
        array = np.append(array, int(new) * pow(10, -lengthNum))
        num = new
    return array

# Метод произведений
def methodMultiplications(core, num, iter, array):
    lengthNum = len(num)

    for i in range(iter):
        mult = str(int(num) * core)

        while len(mult) != lengthNum * 2:
            mult = "0" + mult

        # Список средних разрядов
        new = mult[int(lengthNum - lengthNum / 2): int(lengthNum + lengthNum / 2)]

        # Преобразование в новое число в интервале (0; 1)
        array = np.append(array, int(new) * pow(10, -lengthNum))

        # Получение следующего множимого
        num = mult[-lengthNum:]
    return array

# Мультипликативный конгруэнтный метод
def multiCongMethod(multiplier, divider, iter, num, array):
    lengthNum = len(str(num))

    for i in range(iter):
        # Произведение числа на множитель
        if num == 0:
            mult = multiplier * multiplier
        else:
            mult = multiplier * num

        # Целая часть от деления
        chastnoe = mult // divider
        # Остаток - следующее число
        remainder = mult % divider

        # Преобразование в новое число в интервале (0; 1)
        array = np.append(array, remainder * pow(10, -lengthNum))
        num = remainder
    return array

# Смешанный конгруэнтный метод
def mixedCongMethod(multiplier, const, divider, iter, num, array):
    lengthNum = len(str(num))

    for i in range(iter):
        # Произведение числа на множитель
        if num == 0:
            mult = multiplier * multiplier
        else:
            mult = multiplier * num

        # Следующее число последовательности
        nextNum = round((mult + const) % divider, 4)

        # Случайное число
        new = '0' + str(nextNum)
        array = np.append(array, new)
        num = nextNum
    return array

def main():
    array = np.array([])
    method = 1
    while(method):
        iter = int(input("Количество случайных чисел: "))
        print("--------Выберите метод--------")
        method = int(input("1. Метод квадратов\n"
              "2. Метод произведений\n"
              "3. Мультипликативный конгруэнтный метод\n"
              "4. Смешанный конгруэнтный метод\n"
              "0. Выход\n"))

        if method == 1:
            num = input("Исходное число: ")
            numbers = methodSquares(num, iter, array)
            print(numbers)
            plt.hist(numbers, bins=int(iter / 10))
            plt.xlabel('Случайное значение')
            plt.ylabel('Количество случайных чисел')
            plt.show()
        elif method == 2:
            core = int(input("Ядро: "))
            num = input("Множимое: ")
            numbers = methodMultiplications(core, num, iter, array)
            print(numbers)
            plt.hist(numbers, bins=int(iter / 10))
            plt.xlabel('Случайное значение')
            plt.ylabel('Количество случайных чисел')
            plt.show()
        elif method == 3:
            multiplier = int(input("Множитель: "))
            divider = int(input("Делитель: "))
            num = int(input("Исходное число: "))
            numbers = multiCongMethod(multiplier, divider, iter, num, array)
            print(numbers)
            plt.hist(numbers, bins=int(iter / 10))
            plt.xlabel('Случайное значение')
            plt.ylabel('Количество случайных чисел')
            plt.show()
        elif method == 4:
            multiplier = int(input("Множитель: "))
            divider = int(input("Делитель: "))
            const = int(input("Аддитивная константа: "))
            num = int(input("Исходное число: "))
            number = mixedCongMethod(multiplier, const, divider, iter, num, array)
            print(numbers)
            plt.hist(numbers, bins=int(iter / 10))
            plt.xlabel('Случайное значение')
            plt.ylabel('Количество случайных чисел')
            plt.show()
        else:
            break


if __name__ == '__main__':
    main()