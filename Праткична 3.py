my_bro = {
        "name" : "Serhiy",
        "year" : 16,
        "information" : {
            "city" : "Rozhyshche",
            "country" : "Ukraine",
            "phone" : "redmi",
            "animal" : "dog",
            "class" : 11
        },
        "watch" : "serials",
    }
print(my_bro)

my_bro = {
        "name" : type("Serhiy"),
        "year" : type(16),
        "information" : {
            "city" : type("Rozhyshche"),
            "country" : type("Ukraine"),
            "phone" : type("redmi"),
            "animal" : type("dog"),
            "class" : type(11)
        },
        "watch" : type("serials"),
    }
print(my_bro)