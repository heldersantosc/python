#

cars = {}

cars["corola"] = "red"
cars["fit"] = "green"
cars["vw"] = "black"
cars["hyundai"] = {"cor": "verde"}

print(cars)
print(cars.keys())
print(cars.values())

cars.keys


pessoa = dict(nome="helder", sobrenome="santos")
print(pessoa)
print(pessoa.keys())
print(pessoa.values())


if "nome" in pessoa:
    print(pessoa["nome"])
