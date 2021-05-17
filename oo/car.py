class Car:

    rodas = 4

    def __init__(self):
        self.name = "gol"
        self.year = 2021


class Motocycle:

    rodas = 2

    def __init__(self, name, year):
        self.name = name
        self.year = year

    def drive(self):
        print("%s started" % self.name)

    # metodo estatico que nao depende dos atributos da classe e nem da instância
    @staticmethod
    def hello():
        print("Oi")

    @classmethod
    def exibeRodas(cls):
        print(cls.rodas)


car = Car()
motocycle = Motocycle("XRF", 2020)


print(car.name)
print(motocycle.name)
motocycle.drive()
motocycle.exibeRodas()
