from functools import reduce
numeros= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]



resultado= list(filter(lambda x: x % 2 ,numeros))
resultado.sort()
print(list(resultado))

print(f"suma de datos impares: {reduce(lambda a,b:a+b, resultado)}")
