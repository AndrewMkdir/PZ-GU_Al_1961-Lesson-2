my_list = input("Введите число из списка через пробел: ").split()
print('Введеный список: ', my_list)

idx = len(my_list) if len(my_list) % 2 == 0 else len(my_list) - 1

my_list[:idx:2], my_list[1:idx:2] = my_list[1:idx:2], my_list[:idx:2]
print('Изменяемый список: ', my_list)
