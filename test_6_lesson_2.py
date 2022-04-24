print("create your data structure 'Products'")
n = int(input('enter numbers of members in your list:  '))
ch = int(input('enter number lists:   '))
my_list1 = []
my_list2 = []
my_list3 = []
my_list4 = []
my_list5 = []
i = 1
j = 1
while i <= ch:
    k1 = "product name"
    k2 = input(f"enter product name {i}:    ")
    p1 = "product price"
    p2 = int(input(f"enter product price {i}:   "))
    x1 = "product quantity"
    x2 = int(input(f"enter product quantity {i}:   "))
    y1 = "unit measument"
    y2 = input(f"enter unit measument {i}:   ")
    dict1 = {k1:k2,p1:p2,x1:x2,y1:y2}
    product1 = (i,dict1)
    my_list1.append(product1)
    my_list2.append(k2)
    my_list3.append(p2)
    my_list4.append(x2)
    my_list5.append(y2)
    i = i + 1
for my_list1, el in enumerate(my_list1,1):
    print(my_list1, el)
my_list2 = {k1:my_list2}
my_list3 = {p1:my_list3}
my_list4 = {x1:my_list4}
my_list5 = set(my_list5)
my_list5 = {y1:my_list5}
print(my_list2)
print(my_list3)
print(my_list4)
print(my_list5)

