my_dict = {'sozdanie imperii':1721, 'raspad imperii':1917}
print(my_dict)
print(my_dict.get('sozdanie imperii'))
print(my_dict.get('restavracia monarhii'))
my_dict = {'obrazovanie rsfsr':1918,'obrazovanie cccr':1922}
print(my_dict)
del my_dict['obrazovanie cccr']
print(my_dict)

my_set = {2002, 'pelmen', 'pelmen', 2024, True}
print(my_set)
my_set = {'banan', 100}
print(my_set.discard('banan'))
print(my_set)
