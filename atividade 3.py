print ("Exercício 2")
print()
numero = (int(input("Digite um número: ")))

if numero >= 10 and numero <= 50 :
    print ("Seu número está entre 10 e 50")
if numero < 10 :
    print ("Seu número é menor que 10")
if numero > 50 :
    print ("Seu número é maior que 50")
print()
print ("Exercício 3")
print()
ano = (int(input("Digite um ano para descobrir se ele é bissexto: ")))

if ano % 4 == 0 and ano % 100 != 0 and ano % 400 != 0 : 
        print (str(ano) + " : esse ano é BISSEXTO! ")
else :
     print(str(ano) +" esse ano não é BISSEXTO!")
print()
print ("Exercício 4")

usuario = input("Digite o nome de usuário : ")
senha = (input("Digite sua senha de acesso : "))

if usuario == 'admin' and senha == '1234' :
    print()
    print ("Acesso liberado...")
elif usuario == 'convidado' and senha == '' : 
     print()
     print ("Acesso restrito")
else :
    print()
    print ("Acesso bloqueado!")
print()
print ("Exercício 5")
x = float(input("Digite a coordenada X : "))
y = float(input("Digite a coordenada Y : "))

if 0 < x < 10 and 0 < y < 10 :
    print()
    print ("Dentro do quadrado")
elif 0 == x or x == 10 or y == 0 or y == 10 :
    print()
    print ("Na fronteira")
else :
    print()
    print ("Fora do quadrado")

