# Последовательный поиск числа в списке в виде функции search

# Исходный список расположен в файле input.txt 
fileArray = open("input.txt", "r")
arr = []
for lineArray in fileArray :
    arr.append(int(lineArray))

# Число, которое необходимо ввести для поиска
digit = int(input("Введите число от 1 до 10: "))

# Функция поиска search(список, число)
def search(a, d) :
    for i in range(len(a)) :
        if a[i] == d :
            return i
    return "None"

# Вывод в консоль индекс первого найденного элемента или "None" 
print(search(arr, digit))