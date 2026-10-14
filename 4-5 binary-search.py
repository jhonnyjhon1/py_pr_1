# Алгоритм двоичного поиска
# Первое задание: поиск элемента в списке
# Второе задание: отсутствие элемента

# Исходный список расположен в файле input.txt 
fileArray = open("input.txt", "r")
arr = []
for lineArray in fileArray :
    arr.append(int(lineArray))

# Число, которое необходимо ввести для поиска
digit = int(input("Введите любое число от 1 до 10: "))
# Важное уточнение: для корректной работы список должен быть отсортирован по возрастанию
arr.sort()

low = 0
high = len(arr) - 1

while low < high :
    middle = (low + high) // 2
    if digit > arr[middle] :
        low = middle + 1
    else :
        high = middle

if arr[low] == digit :
    # Выводит в консоль индекс заданного числа
    print("Есть под номером ", low)
else :
    # Вывод в консоль если число не найдено
    print("Нет такого")