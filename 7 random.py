# Импорт библиотеки генерации для случайных чисел
import random  

# Входные параметры вводимые с консоли: число, левая и правая границы списка
count = int(input("Введите кол-во элементов для списка: "))
firstInt = int(input("Введите левую границу массива: "))
secondInt = int(input("Введите правую границу массива: "))

# Проверка на корректные границы массива 
num = False
while num is False :
    if secondInt <= firstInt :
        secondInt = int(input("Правая граница должна быть больше левой, введите еще раз: "))
        num = False
    else :
        num = True

# Генерация случайного списка 
arr = [random.randint(firstInt, secondInt) for i in range(count)]

# Запись в файл output.txt случайно сгенерированный список
fileArray = open("output.txt", "w")
for i in range(len(arr)) :
    fileArray.write(str(arr[i]) + '\n')

fileArray.close()