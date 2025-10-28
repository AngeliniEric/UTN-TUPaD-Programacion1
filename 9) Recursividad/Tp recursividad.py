# 1) Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa
# función para calcular y mostrar en pantalla el factorial de todos los números enteros
# entre 1 y el número que indique el usuario
print("\n---------- Ejercicio 1 ----------\n")

def factorial(x):
    if x == 0:
        return 1
    else:
        fact = x * factorial(x-1)
        return fact

num = int(input("Ingrese un número: "))
for i in range(num+1):
    fact = factorial(i)
    print(f"Factorial de {i}: {fact}")

input("\nPresione Enter para continuar. ")

# 2) Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición
# indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario
# especifique.
print("\n---------- Ejercicio 2 ----------\n")

def fibonacci(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else: 
        return fibonacci(x-1) + fibonacci(x-2)

num = int(input("Ingrese un número. "))
for i in range(num+1):
    print(f"Posición {i}: {fibonacci(i)}")

input("\nPresione Enter para continuar. ")

# 3) Crea una función recursiva que calcule la potencia de un número base elevado a un
# exponente, utilizando la fórmula 𝑛(𝑚) = 𝑛 ∗ 𝑛(𝑚−1). Prueba esta función en un
# algoritmo general.
print("\n---------- Ejercicio 3 ----------\n")

def potencia(base,exponente):
    if exponente == 0:
        return 1
    else: 
        resultado = base * potencia(base,exponente-1)
        return resultado

x = int(input("Ingrese la base: "))
y = int(input("Ingrese el exponente: "))
print(f"{x} elevado a {y} = {potencia(x,y)}")

input("\nPresione Enter para continuar. ")

# 4) Crear una función recursiva en Python que reciba un número entero positivo en base
# decimal y devuelva su representación en binario como una cadena de texto.
print("\n---------- Ejercicio 4 ----------\n")

def binario(x):
    if x == 0:
        return "0"
    elif x == 1:
        return "1"
    else:
        resto = x % 2
        actual = x // 2
        return binario(actual) + str(resto)

decimal = int(input("Ingrese un número que desea pasar a binario: "))
print(f"{decimal} en binario = {binario(decimal)}")

input("\nPresione Enter para continuar. ")

# 5) Implementá una función recursiva llamada es_palindromo(palabra) que reciba una
# cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no
# lo es.
# Requisitos:
# La solución debe ser recursiva.
# No se debe usar [::-1] ni la función reversed().
print("\n---------- Ejercicio 5 ----------\n")

def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    elif palabra[0] != palabra[-1]:
        return False
    else: 
        return es_palindromo(palabra[1:-1])
    
palabra = input("Ingrese una palabra: ")
if es_palindromo(palabra) == True:
    print("Es palíndromo. ")
else: 
    print("No es palíndromo. ")

input("\nPresione Enter para continuar. ")

# 6) Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un
# número entero positivo y devuelva la suma de todos sus dígitos.
# Restricciones:
# No se puede convertir el número a string.
# Usá operaciones matemáticas (%, //) y recursión.
# Ejemplos:
# suma_digitos(1234) → 10 (1 + 2 + 3 + 4)
# suma_digitos(9) → 9
# suma_digitos(305) → 8 (3 + 0 + 5)
print("\n---------- Ejercicio 6 ----------\n")

def suma_digitos(n):
    if n < 10:
        return n
    else:
        ultimo = n % 10
        actual = n // 10
        acumulador = ultimo + suma_digitos(actual)
        return acumulador

num = int(input("Ingrese un número: "))
print(f"La suma de dígitos de {num}: {suma_digitos(num)}")

input("\nPresione Enter para continuar. ")

# 7) Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n
# bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al
# último nivel con un solo bloque.
# Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el
# nivel más bajo y devuelva el total de bloques que necesita para construir toda la
# pirámide.
# Ejemplos:
# contar_bloques(1) → 1 (1)
# contar_bloques(2) → 3 (2 + 1)
# contar_bloques(4) → 10 (4 + 3 + 2 + 1)
print("\n---------- Ejercicio 7 ----------\n")

def contar_bloques(x):
    if x == 1:
        return 1
    else:
        total = x + contar_bloques(x-1)
        return total

num = int(input("Ingrese la cantidad de bloques en la base: "))
print(f"Cantidad de bloques necesarios para la pirámide: {contar_bloques(num)}")

input("\nPresione Enter para continuar. ")

# 8) Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un
# número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces
# aparece ese dígito dentro del número.
# Ejemplos:
# contar_digito(12233421, 2) → 3
# contar_digito(5555, 5) → 4
# contar_digito(123456, 7) → 0
print("\n---------- Ejercicio 8 ----------\n")

def contar_digito(numero,digito):
    if numero == 0:
        return 0
    else: 
        ultimo = numero % 10
        actual = numero // 10
        contador = contar_digito(actual,digito)
        if ultimo == digito:
            return 1 + contador
        else: 
            return 0 + contador
        

num = int(input("Ingrese un número: "))
dig = int(input("Ingrese un dígito: "))
print(f"Cantidad de veces que el dígito {dig} aparece en el número {num}: {contar_digito(num,dig)}")

input("\nPresione Enter para continuar. ")