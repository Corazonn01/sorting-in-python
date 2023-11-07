# sorting-in-python
#how to sort by asc, desc and none 

#from a to z (asc)
num = [1, 8, 9, 5, 2, 6, 7]
sorted_num = sorted(num)
print(sorted_num)

#same with alphabet
alphabet = ['e', 'l', 'i', 'n', 'a']
sorted_alph = sorted(alphabet)
print(sorted_alph)

#reversed (in opposide order ) (desc)
letter = ['a', 's', 'r', 'b', 'o', 'c']
sorted_letters = sorted(letter, reverse = True)
print(sorted_letters)

#same way but diffrent code 
number = [1, 88, 9, 100, 7, 0]
print(sorted(number, reverse = True))

#with None 
for i in number:
    print(i)  #none does not mean "nothing", it means "no order", it will be by default like u wrote 
