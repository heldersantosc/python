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
