a = 8
b = "Hello"
c = 17
d = 99

list = [a, b, c, d]
print(list)
list = [type(a), type(b), type(c), type(d)]
print(list)

list_type_more = max(list, key=list.count)
print(list_type_more)