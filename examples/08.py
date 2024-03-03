# Тип №8 использует основные формулы по комбинаторике
# С ними можно познакомиться здесь https://habr.com/ru/articles/479816/
# и здесь https://habr.com/ru/companies/otus/articles/529356/

# Тип №8. Подсчет количества разных последовательностей
# Задание №10473
# Задания для самопроверки: №10500

# В задачах этого типа очень часто нужно использовать библиотеку itertools
# А в частности функцию product (размещения с повторениями)
from itertools import product 

# Сколько различных вариантов шифра можно задать, ...
count = 0

# Шифр кодового замка представляет собой последовательность из пяти символов (repeat = 5),
# каждый из которых является цифрой от 1 до 4. (первый аргумент в функции product "1234")
for p in product("1234", repeat=5):    

    # ... если известно, что цифра 1 встречается ровно два раза,
    if p.count('1') == 2:
        count += 1

print(count)

'''
Пояснения: 
С помощью встроенной функции count() мы можем считать количество повторений элемента в
строке или массиве

Пример:
stroka = "sobaka"
print(stroka.count("a")) # Вывод: 2

'''

# Тип №8. Подсчет количества разных последовательностей
# Задание №58240
# Задание для самопроверки: №58237

# В этой задаче все цифры должны идти в убывающем порядке (внимание: НЕ в невозрастающем)
# Т.е. 77533 считаться не будет. Значит мы должны искать размещения без повторений
# Можно использовать функцию permutations (перестановки)
from itertools import permutations

# Сколько существует ...
count = 0

# ... различных пятизначных чисел, (repeat = 5) 
# записанных в девятеричной системе счисления 
# (первый аргумент в функции product "012345678") ...
for p in permutations("012345678", 5):    
    if p[0] == "0":
        continue

    # ... в записи которых цифры следуют слева направо в убывающем порядке
    if list(p) == sorted(p)[::-1]:
        count += 1

print(count)

'''
Пояснения: 
sorted() - функция, которая сортирует массив в строго алфавитном порядке, 
а нам нужен убывающий порядок. Значит нужно развернуть с помощью [::-1] (отриц. шаг)

permutations и sorted возвращают разные типы массивов (это можно понять как минимум по скобочкам при выводе)
Чтобы их сравнить я p привожу в тип list, а sorted(p)[::-1] не трогаю
'''

# Тип №8. Подсчет количества разных последовательностей
# Задание №58240
# Задание для самопроверки: №58237

# Определите количество ... 
count = 0

# ... четырехзначных чисел (второй аргумент в функции permutations),
# записанных в десятичной системе счисления, (первый аргумент "0123456789")
# в записи которых все цифры различны (поэтому используем permutations) ...
for p in permutations("0123456789", 4):
    if p[0] == "0":
        continue

    s = "".join(p)
    s = s.replace("0", "!").replace("2", "!").replace("4", "!").replace("6", "!").replace("8", "!")
    s = s.replace("1", "@").replace("3", "@").replace("5", "@").replace("7", "@").replace("9", "@")
    
    # и никакие две чётные и две нечётные цифры не стоят рядом.
    if "@@" in s or "!!" in s:
        continue
    
    count += 1

print(count)