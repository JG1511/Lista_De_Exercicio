salario = float(input("Digite seu salario: "))

if salario <= 1903.98:
    print("Isento de imposto de renda") 
elif 1903.99 <= salario <= 2826.65:
    print("O imposto de renda a ser pago é: ", (salario * (7.5 /100)) + salario)
elif 2826.66 <= salario <= 3751.05:
     print("O imposto de renda a ser pago é: ", (salario * (15 /100)) + salario)
elif 3751.06 <= salario <= 4664.68:
     print("O imposto de renda a ser pago é: ", (salario * (22.5 /100)) + salario)
else:
      print("O imposto de renda a ser pago é: ", (salario * (27.5 /100)) + salario)