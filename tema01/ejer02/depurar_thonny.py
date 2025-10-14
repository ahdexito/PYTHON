def calcular_suma_par(numeros):
    resultado = 0
    for numero in numeros:
        if numero % 2 == 0:
            resultado += numero
    return resultado

lista = [1, 2, 3, 4, 5, 6]
print(calcular_suma_par(lista)) # Salida esperada: 12, pero el resultado será 6