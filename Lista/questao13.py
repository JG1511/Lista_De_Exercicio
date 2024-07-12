var_entrada = int(input("Digite um valor de entrada: "))
var_mult = 1
var_total = 0
var_str = ""

for i in range(11):
    var_total = var_entrada * var_mult
    

    if i == 0:
        var_str += str(var_entrada)
    else:
        var_str += f" X {var_mult}"
        var_mult +=1

    print(f"A tabuada: {var_str} = {var_total}")

    