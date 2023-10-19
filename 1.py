a = input("Цепочка 1 ")
b = input("Цепочка 2 ")

list1 = a.split(' ')
list2 = b.split(' ')

print("result:")

for ch1 in list1:
    for ch2 in list2:
        print((ch1 + ch2) + " ") 