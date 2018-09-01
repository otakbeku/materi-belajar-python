"""
built-in data types:
1. String
2. Numeric: integer & float
3. Boolean: True or False
4. Sequence: List, Set, Tuple
5. Mapping: Dictionary

1. String: Bisa dibentuk dari 4 contoh berikut:
"""
petik_1 = 'Teks'
petik_ganda = "Teks"
petik_3 = '''Teks'''
petik_3_ganda = """Teks"""

'''
Numeric: integer & float

integer nilainya atau besarnya bergantung pada ukuran memori, 
jadi selama ada memori yang besar, naruh berapa pun bisa
'''
integer_1 = 1
integer_2 = 12
print(type(integer_1))  # Hasilnya int

# Float punya koma dan lebih besar nilainya
float_1 = 1.
float_2 = 12.
print(type(float_1))  # Hasilnya float

from fractions import Fraction

f = Fraction(16, 8)
print(f.numerator)
print(f.denominator)

print(16 / 5)  # True Division
print(16 // 5)  # Integer Division

# Bilangan kompleks
c = 12. + 14j
print(c.real)  # nilai realnya
print(c.imag)  # nilai imajinernya

'''
Boolean

Cuma True or False ...

NEXT

Sequence
1. List
'''
list_1 = [1, 1, 1, 2, 3, 234, 4, 7, 2, 45, 10, 34]
print(list_1)
list_1.append(12)  # Nambah item
list_2 = list_1.copy()  # Ngopi
print(list_1.count(1))  # jumlah element 1

'''
2. Set
'''
set_1 = set(list_1)
set_2 = {1, 2, 3, 4, 7, 10, 34, 45, 234}
set_1.add(5)  # nambah elemen

'''
3. Dictionary
'''
dict_1 = {'item1': 1, 'item2': 2}
dict_1['item3'] = 3  # nambah elemen

'''
4. Tuple
'''
t_3 = (1, 2, 3)
print(t_3.count(3))  # Ngitung element tersebut di tuple

'''
Input dalam python
'''
input_1 = input('Tulis teks: ')
print(input_1)  # hasil dari input
