# Список користувачів
users = [
    ['Micle', 28, 'активний'],
    ('Bob', 22, 'неактивний'),
    ('Charlie', 35, 'активний'),
    ('David', 19, 'неактивний')
]
status = input('Введіть статус для обчислення середнього віку: ')

sum_years = 0
count = 0
for user in users:
    if status == user[2]:
        sum_years += user[1]
        count += 1

print(sum_years/count)