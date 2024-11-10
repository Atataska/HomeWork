def print_params(a=1, b='строка', c=True):
    print(a, b, c)
print_params(9, 'таблица', False)
print_params(6, 'Есть')
print_params(a='Самолет', b='восемь', c='три')
print_params(a='11', b='Urban')
print_params(b='два', c='три')
print_params(a='4', c='Собака')
print_params(a='Сова')
print_params(b='Кошка')
print_params(c='10')
print_params()


print_params(b=25)
print_params(c=[1, 2, 3])

values_list = [ 5, 'Cat', 2.3]
values_dict = {'a': 7, 'b': 'merion', 'c': 3 }
print_params(*values_list)
print_params(**values_dict)

values_list_2 = [54.32, 'Строка' ]
print_params(*values_list_2, 42)
