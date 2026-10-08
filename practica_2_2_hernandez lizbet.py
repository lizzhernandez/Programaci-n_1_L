#par o impar 
numero = 11
es_par = numero % 2 == 0
print(f"El numero {numero} es par: {es_par}")

#ejercicio 2
numero1= "8" 
numero2= "3"
print("Suma de texto: " + numero1 + numero2)
suma= int(numero1) + int(numero2)
print("Suma de numeros: " + str(suma))
#ejercio 3
nombre = "Lizbet" 
edad = 20
estatura= 1.70
es_estudiante = True
print("nombre:",nombre, type(nombre))
print("edad:",edad, type(edad))
print("estatura:",estatura, type(estatura))
print("es estudiante:",es_estudiante, type(es_estudiante))
#ejercicio 4
a=31
b=11
print("Division entera (//):",a//b)
print("Residuo(%):",a%b)
#ejercicio 5
a=16
b=16
mayor = a > b
menor = a < b
igual = a == b
print("Mayor, menor, igual:", mayor, menor, igual)
#operadores logicos
cond1= 31>11
cond2 = 4=4
cond3 = 5<3
and_result = cond1 and cond2
or_result = cond1 or cond3
not_result = not cond1
print("Resultado AND:", and_result)
print("Resultado OR:", or_result)
#promedio y aprobacion
cal1 = 8.5
cal2 = 9.0
cal3 = 7.5
promedio = (cal1 + cal2 + cal3) / 3
aprobado = promedio >= 7.0
print("Promedio:", promedio)
print("Aprobado:", aprobado)
#Validacon de elegibilidad
edad = 20
nacionalidad = "mexicano"
es_elegible = edad >= 18 and nacionalidad == "mexicano"
print("Es elegible (AND):", es_elegible)