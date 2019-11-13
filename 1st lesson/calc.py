value_one = int(input("Хей, введи мне циферку!\n"))

print("+ сложить")
print("- вычесть")
print("/ разделить")
print("* умножить")

operation = input("Введите операцию\n")

value_two = int(input("Хей, мне нужна ещё одна цифра!\n"))

if operation == "+":
    print(value_one + value_two)
elif operation == "-":
    print(value_one - value_two)
elif operation == "/":
    print(value_one / value_two)
elif operation == "*":
    print(value_one * value_two)
else:
    print("Я не знаю такой операции!")
