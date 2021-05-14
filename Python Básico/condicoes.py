# exemplicando as condições com if e else

total = 100

if total > 100:
    print("Maior que 100")
elif total < 50:
    print("Menor que 50")
else:
    print("Não é maior que 100 e nem menor que 50")


nome_completo = "Helder Santos"

for nome in nome_completo:
    if not nome == "a":
        print("Não é igual")

for nome in nome_completo.split(" "):
    if not nome == "Helder":
        print(nome, "\nNão é igual a Helder")
