#ejercicio clasificacion por edad 
edad = int(input("escribe tu edad: "))
if edad < 13 :
        print("menor")
elif edad < 17 :
        print("adolecnte")
else :
        print("mayor")

#ejercicio validar acceso y contraseña 
usuario_correcto=input("ingresa usurio:")
contraseña_correcta=input("ingresa contraseña:")
if usuario_correcto == "lizbet" and contraseña_correcta == "113115":
    print ("acesso correcto ")
elif usuario_correcto == "lizbet" and contraseña_incorrecta == "" : 
    print("contraseña incorrecta")
else : 
    print("acceso denegado")

#calculadora de envio 
peso = float (input ("ingresa el peso del paquete:"))
costo = 0 
if peso <= 1 :
    costo = 50 
elif peso <= 5 :
    costo = 90 
else :
    costo =160

if peso > 10 :
    costo = costo * 0.90 
print ("el costo sera ", costo)

#clasificacion de temperatura 
temperatura = float (input ("ingresa la temperatura en grados : "))
if temperatura < 10 :
    print ("frio")
elif temperatura <25 :
    print ("templado")
else :
    print ("calor")

#clasificacion con letras 
calificacion = float ( input ("ingresa tu calificacion del 0 al 100: "))
if calificacion < 0 or calificacion > 100 :
    print ("calificaion no valida")
elif calificacion >= 90 :
    print ("Calificacion A")
elif calificacion >= 80 :
    print ("Calificaion B")
elif calificacion >= 70 :
    print ("Calificaion C")
elif calificacion >= 60 :
    print("Califiacion D")
else :
    print("No aprobado F ")

#Descuento por monto de compra 
compra = float (input("ingrese el monto de compra $: "))
if compra > 500 :
    descuento = 20
elif compra > 200 :
    descuento = 10
else:
    descuento = 0 
monto_descuento = compra * descuento / 100 
total = compra - monto_descuento
print ("Porcentaje de descuento:", descuento ,"%")
print ("Monto del descuento:", monto_descuento)
print ("Total a pagar : $", total)

#Calcular un rango on comparacion encadenada 
numero = float (input("ingresa un numero: "))
if 1<= numero <= 100 :
    print("el numero de rango es")
else :
    print ("no esta dentro del rango ")

#Clasificar el IMC
peso_imc = float (input("ingresa el peso en kg: "))
estatura = float (input ("ingresa la estatura en metro :"))
if peso_imc <=0 or estatura <=0 :
    print ( " el peso y la estaura debe de ser mayor a cero ")
else :
    imc= peso_imc / estatura ** 2
    print ("Tu IMC es:", round (imc, 2) )
if imc < 18.5: 
    print("Clasificaion: bajo peso")
elif imc < 25 :
    print ("Clasificaion : normal ")
elif imc < 30 :
    print ("Clasificacion : sobrepeso")
else:
    print ("Clasificacion : obecidad")

#Tarifas de electriciada 
consumo = float ( input ( "ingreesa el consumo mensual n kwh: "))
if consumo < 0 :
    print ("el consumo no puede ser negativo ")
elif consumo <=150 :
    costo_total = consumo * 1.20 
elif consumo <= 300:
    costo_total = (150 * 1.20 ) + ((consumo - 150 )*1.80)
else : 
    costo_total= (
        (150 * 1.20)
        + (150 * 180)
        + ((consumo - 300 )* 2.50)
    )
if consumo >= 0 :
    print ("Consumo mensual :", consumo , "kwh")
    print ("Coato total : $ ", round (costo_total , 2 ))
    