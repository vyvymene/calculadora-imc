peso = float(input("Digite o seu peso: "))
altura = float(input("Digite a sua altura: "))

#calculo de IMC:

imc = peso / altura ** 2


if imc < 18.5:
   print("Abaixo do peso")
elif imc < 25:
   print("Peso normal")
elif imc < 30:
   print("Sobrepeso")   
else:
   print("Obesidade")     

print(f"Seu IMC é: {imc:.2f}")   