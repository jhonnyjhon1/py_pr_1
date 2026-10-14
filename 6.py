# Алгоритм двоичного поиска в списке в виде функции binary_search

# Исходный список расположен в файле input.txt 
fileArray = open("input.txt", "r")
arr = []
for lineArray in fileArray :
    arr.append(int(lineArray))

# Число, которое необходимо ввести для поиска
digit = int(input("Введите любое число от 1 до 10: "))
# Важное уточнение: для корректной работы список должен быть отсортирован по возрастанию
arr.sort()

# Функция поиска binary_search(список, число)
def binary_search(a, d) :
    low = 0
    high = len(a) - 1
    
    while low < high :
        middle = (low + high) // 2
        if d > arr[middle] :
            low = middle + 1
        else :
            high = middle
    
    if arr[low] == d :
        return ("Есть под номером " + str(low))
    else :
        return "Нет такого"    

# Вывод в консоль индекс первого найденного элемента или "Нет такого"     
print(binary_search(arr, digit))    