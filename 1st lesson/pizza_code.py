word = "Хочу заказать пять пицц пеперони"

col_three = { "один": 1, "три": 3, "пять" : 5}

for item in word.split(" "):
    if item in col_three:
        print(col_three[item])