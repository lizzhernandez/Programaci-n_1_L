#while- NO SE SABE DE ANTEMANO CUANTAS VECES
contador = 0
while contador < 5 :
    print("contador:", contador)
    contador = contador + 1

#no sabe cuantos intentos hara la persona 
# ! = diferente de
clave = ""
while clave != "1234" :
    clave = input(" Contraseña: ")
print("acceso permitido")

#lower es para minusculas , el progrma lo convierte a minusculas y asi no importa si la persona escribe en mayusculas o minusculas
#upper es para mayusculas, el programa lo convierte a mayusculas y asi no importa si la persona escribe en mayusculas o minusculas
while True :
    print("Se ejecuta al menos una vez")
    user_input = input("¿Continuar? (y/n): ")
    if user_input.lower() != 'y': #upper ()        
        break

#sin inciciar falla
# for _ in range(5) :
#.    contador = contador + 1
#print (contador)
#simpre la misma cantidad , correcta 
contador = 0
for _ in range(5) :
    contador = contador + 1
print(contador)

#acumulador - suma un valor que cambia 
precios = [50, 120, 30]
total = 0
for precio in precios:
    total = total + precio
print(total)

precios = [ 30,10,9,50,29,10]
total = 0
for precio in precios :
    print (precio)

#matriz - accede con dos indices
matriz = [
    [1,2,3 ],
    [4,5,6]
]
print(matriz [0][0]) #1
print(matriz [0][1]) #2
print(matriz [0][2]) #3
print(matriz [1][0]) #4
print(matriz [1][1]) #5
print(matriz [1][2]) #6

matriz = [
    ["s","o","r","p"],
    ["r","e","s"]
]
print(matriz [0][0]) #s
print(matriz [0][3]) 

# incertar  -append() y insert(), 
#append() agrega al final de la lista, insert() agrega en la posicion que se indique
frutas = ["manzana", "pera" ]
frutas.append("uva")
frutas.insert(1, "kiwi")
print(frutas)

#eliminar - pop() y remove()
frutas.remove("pera") #elimina por valor
frutas.pop(0) #elimina por indice
del          frutas[0] #elimina por indice
print(frutas)

#busqueda -in e index()
frutas = ["manzana", "pera", "uva"]
print("pera" in frutas) #True
print(frutas.index("uva")) #2 te marca en que posicion esta el valor que buscas

