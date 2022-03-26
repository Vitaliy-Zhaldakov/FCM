# Нечётные - больше половины
# Чётные - меньше половины

# Метод квадратов
def methodSquares(num, iter):
    if iter != 0:
        squareNum = num * num
        lengthNum = len(str(num)) / 2
        # Список цифр
        listDigits = list(str(squareNum))
        if len(listDigits) % 2 != 0:
            listDigits.insert(0, '0')

        # Список средних разрядов
        midDigits = listDigits[int(lengthNum): len(listDigits) - int(lengthNum)]

        # Преобразование в новое число в интервале (0; 1)
        new = float(''.join(map(str, ['0', '.'] + midDigits)))
        print(f"Случайное число: {new}")
        methodSquares(int(''.join(map(str, midDigits))), iter - 1)

# Метод произведений
def methodMultiplications(core, num, iter):
    if iter != 0:
        print(f"Множимое: {num}")
        lengthNum = len(str(num)) / 2
        mult = core * num

        # Список цифр
        listDigits = list(str(mult))
        if len(listDigits) % 2 != 0:
            listDigits.insert(0, '0')

        # Список средних разрядов
        midDigits = listDigits[int(lengthNum): len(listDigits) - int(lengthNum)]
        # Преобразование в новое число в интервале (0; 1)
        new = float(''.join(map(str, ['0', '.'] + midDigits)))
        print(f"Случайное число: {new}\n")

        # Получение следующего множимого
        nextNum = int(''.join(map(str, listDigits[-len(str(num)):])))
        methodMultiplications(core, nextNum, iter - 1)

# Мультипликативный конгруэнтный метод
def multiCongMethod(multiplier, divider, iter, num):
    if iter != 0:
        # Произведение числа на множитель
        if num == 0:
            mult = multiplier * multiplier
        else:
            mult = multiplier * num

        # Целая часть от деления
        chastnoe = mult // divider
        print(f'Частное: {chastnoe}')
        # Остаток - следующее число
        remainder = mult % divider

        # Преобразование в новое число в интервале (0; 1)
        new = float('0.' + str(remainder))
        print(f"Случайное число: {new}\n")
        multiCongMethod(multiplier, divider, iter - 1, remainder)

# Смешанный конгруэнтный метод
def mixedCongMethod(multiplier, const, divider, iter, num):
    if iter != 0:
        # Произведение числа на множитель
        if num == 0:
            mult = multiplier * multiplier
        else:
            mult = multiplier * num

        # Следующее число последовательности
        nextNum = (mult + const) % divider

        # Случайное число
        new = float('0.' + str(nextNum))
        print(f'Случайное число: {new}')
        mixedCongMethod(multiplier, const, divider, iter - 1, nextNum)

def main():
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
            num = int(input("Исходное число: "))
            methodSquares(num, iter)
        elif method == 2:
            core = int(input("Ядро: "))
            num = int(input("Множимое: "))
            methodMultiplications(core, num, iter)
        elif method == 3:
            multiplier = int(input("Множитель: "))
            divider = int(input("Делитель: "))
            num = int(input("Исходное число: "))
            multiCongMethod(multiplier, divider, iter, num)
        elif method == 4:
            multiplier = int(input("Множитель: "))
            divider = int(input("Делитель: "))
            const = int(input("Аддитивная константа: "))
            num = int(input("Исходное число: "))
            mixedCongMethod(multiplier, const, divider, iter, num)
        else:
            break


if __name__ == '__main__':
    main()