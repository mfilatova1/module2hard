numbers = int(input("Введите число от 3 до 20: "))
numbers2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
result = []
if numbers in range(0, len(numbers2)+1):
    for i in range(1, len(numbers2)):
        for j in range(i+1, len(numbers2)):
            if numbers % (i+j) == 0:
                result.extend([i, j])
print(numbers, '-', *result)















