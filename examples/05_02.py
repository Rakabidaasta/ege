# Тип №5. Посимвольное десятичное преобразование
# Задание №15101
# Задание для самопроверки: №15128

# Автомат получает на вход четырёхзначное число (число не может начинаться с нуля)
def f(n):
    # Чтобы обращаться к цифрам числа по индексам, составим массив (пояснения ниже)
    numbers = [int(x) for x in str(n)]

    # 1.  Складываются отдельно первая и вторая, ...
    sum12 = numbers[0] + numbers[1]

    # ... вторая и третья, ...
    sum23 = numbers[1] + numbers[2]

    # ... третья и четвёртая цифры заданного числа.
    sum34 = numbers[2] + numbers[3]

    # Для дальнейших действий нам потребуется массив всех сумм
    sums = [sum12, sum23, sum34]

    # 2. Наименьшая из полученных трёх сумм удаляется. Чтобы найти наименьшую, отсортируем
    sums.sort()

    # И теперь удаляем наименьшую (то есть самую первую)
    sums = sums[1:]
    
    # 3. Оставшиеся две суммы записываются друг за другом в порядке неубывания без разделителей.
    # Мы итак уже отсортировали, осталось только записать друг за другом
    r = "".join(str(s) for s in sums)

    return r

# Укажите наименьшее число, ...
for n in range(1000, 10000):
    # ... при обработке которого автомат выдаёт результат 1215.
    # Сравниваем с тем типом данных, который возвращает функция (т.е. со строкой)
    if f(n) == "1215":
        print(n)
        break

'''
Массив можно записать в кратком виде с помощью цикла for 
    [действие for итератор in итерируемый объект]

Пример: 
numbers = [x for x in range(10)]
print(numbers) # Вывод: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

В нашем случае мы проходимся по строковому представлению числа n 
и мы будем перебирать все цифры числа. Затем с помощью функции int() мы преобразуем 
этот символ в число (по сути поменяем тип данных с str на int)
numbers = [int(x) for x in str(n)]

Разбор поэтапно (пусть n = 1234): 
1) str(n) это "1234"
2) for x in str(n), x будет принимать значения "1", "2", "3", "4"
3) int(x) for x in str(n), int(x) будет принимать значения 1, 2, 3, 4 соответственно
4) [int(x) for x in str(n)], составляем массив -> [1, 2, 3, 4]

Пояснение для 30 строчки: r = "".join(str(s) for s in sums)

Надеюсь, из вышенаписанного понятно, как работает сокращенный формат записи массива
Теперь про join (соединить) - функцию для слияния строк.

Поставить друг за другом числа мы не можем, а строки да, 
поэтому и преобразуем все суммы в строки.

Пример работы join: 
print("-ик-".join(["Я", "что-то", "не", "то", "съел"])) # Я-ик-что-то-ик-не-ик-то-ик-съел

Так как нам не нужны разделители, то в качестве соединения стоит пустая строка.
'''

