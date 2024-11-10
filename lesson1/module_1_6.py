my_dict = {'Иван': 1983, 'Вера': 1974, 'Оля': 2001, 'Егор': 1964}

print (my_dict)
print (my_dict['Иван'])
print (my_dict.get('Лиза'))
my_dict.update({'Саша': 1953, 'Леша': 2005})
print (my_dict)
a=my_dict.pop ('Вера')
print (my_dict)
print (a)
print (my_dict)

my_set= {9,8,7,6,5,8,6}
print (my_set)
my_set.update([3,4])
print (my_set)
my_set.remove(9)
print (my_set)