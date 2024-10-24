my_bro = {
        "name" : "Serhiy",
        "year" : 16,
        "information" : {
            "city" : "Rozhyshche",
            "country" : "Ukraine",
            "phone" : "redmi",
            "animal" : "dog",
            "class" : 11},
        "watch" : "serials",}

type_items = {}
for k, v in my_bro.items():
    if type(v) == dict:
        for k1, v1 in v.items():
            type_items[k1] = type(v1)
    else:
        type_items[k] = type(v)
print(type_items)
