# definindo funcao e chamando


def call_number():
    for number in range(0, 10):
        print(number)


call_number()

print("---------------")


def call_number_with_limit(limit):
    list = range(0, 10)

    for number in list[0:limit]:
        print(number)


call_number_with_limit(5)


print("---------------")


def calculator(x, y):
    soma = x + y
    return soma


soma = calculator(20, 4)
print(soma)

soma = calculator(y=10, x=5)
print(soma)
