print ("Exercício 1 ")
print ()
anoNascimento = int(input ("Informe o ano do seu nascimento:"))
print ("Você tem " + str(2026 - anoNascimento) + " anos " )
print ()



print ("Exercício 2")
print ()
valorAluguel = float(100.00)
diasLocados = int(input ("Dias de Locação do Veículo: "))
total = (valorAluguel * diasLocados)
print (f"Valor Total do Aluguel: R$ {total:.2f}")
print ()



print ("Exercício 3")
print ()
temperaturaC = float(input("Temperatura (°C): "))
temperaturaF = (float(temperaturaC * 9/5)+32)
print ("Temperatura atual: " + str(temperaturaF) + "°F")
print ()



print ("Exercício 4")
print ()
nota1 = float (input("Nota A: "))
nota2 = float (input("Nota B: "))
nota3 = float (input("Nota C: "))
nota4 = float (input("Nota D: "))
média = ((nota1 + nota2 + nota3 + nota4) / 4)
print (f"Média : {média:.2f}")
print ()



print ("Exercício 5")
print()
idade = int(input ("Digite sua idade: "))
print ("Equivale a " + str(idade * 12) + " meses")
print ()


print ("Exercício 6")
print ()
preco = float(input ("Preço do produto (R$): "))
peso = float(input ("Peso do produto (g): "))
precoKG = float(preco * 1000) / peso
print (f"R$ {precoKG:.2f} Por KG")
