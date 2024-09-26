
numeros = list(range(1, 101))


resultado = []


for num in numeros:
    if (num % 3 == 0) and (num % 5 == 0):
        resultado.append("fizzbuzz")
    elif num % 3 == 0:
        resultado.append("fizz")
    elif num % 5 == 0:
        resultado.append("buzz")
    else:
        resultado.append(num)

 
for item in resultado:
    print(item)
