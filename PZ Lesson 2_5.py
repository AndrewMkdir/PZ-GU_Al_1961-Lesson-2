rating = [9, 8, 8, 7, 5, 5, 4, 4, 2, 1, 1, 0]
new_rate = int(input('Введите новое число: '))
print(f'Исходный список : {rating}')
max_num = max(list(filter(lambda num: new_rate > num, rating)))
rating = rating[:rating.index(max_num)] + [new_rate] + rating[rating.index(max_num):]
print(f'Новый список    : {rating}')