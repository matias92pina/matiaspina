#Seguimos con Complejidad. 

#Armar una función que imprima  todos los números del 0 al 100 que sean divisbles por 3

#def exercise3():
#    for number in range (0,101): #--> complejidad n
#        if number % 3==0: #--> complejidad 1 (constante)
#            print(number)
#exercise3() #O(n)

##Función que me de 10 números, y los ordene
#def exercise5():
#    userValueList=[] #--> 1
#    for number in range(10): #--> n
#        userValue= int(input("Ingrese un número entero")) #--> 1
#        userValueList.append(userValue) #--> O(1)
    
#    userValueList.sort() #--> n log(n)
#    print(userValueList)
#exercise5() #O(n log(n))
##-------------#
#def exercise6(number1, number2):
#    #comparación de números
#exercise6() #O(1)

#En un peaje tenemos una camara que cuenta el número de vehículos que pasan calculando las rayas
#y las gomas que pasan por las mismas. Crear el algoritmo. 

#vehículos = coches + motos
#ruedas = coche*4 + moto*2 (cantidad de ruedas en total)

#def cochesYmotos (vehiculos, ruedas):
#    for coche in range(vehiculos+1): ##n
#        for moto in range (vehiculos+1): ##n #Vamos uno por uno los vehículos que pasan para calcular si la cuenta nos da la cantidad de ruedas. 
#            if (coche+moto==vehiculos) and (coche*4+moto*2==ruedas): #Constante, porque depende los valores de arriba
#                print(coche*4,"+",moto*2,"=", ruedas)
#                return coche, moto
##O(n^2) -- Cuadrática Orden de complejidad. 
#print(cochesYmotos(60,200)) #6 vehiculos y 20 ruedas

#vehículos = coches + motos --> motos= vehiculos- coches
#def cochesYmotos(vehiculos, ruedas):
#    for coche in range(vehiculos+1): ##n
#        moto=vehiculos-coche #Tener un ciclo menos, reduce muchísimo la cantidad de operaciones
#        if (coche+moto==vehiculos) and (coche*4 + moto*2 == ruedas):
#            print(coche*4,"+",moto*2,"=", ruedas)
#            return coche, moto
##O(n) -- Lineal
#print (cochesYmotos(6,20))

#ruedas = coche*4 + moto *2
#ruedas = coche * 4 + (vehiculos- coches)*2 -->Mucho más simplificado
    #4coche + 2vehiculos-2coche=ruedas --> 2coche + 2vehiculo=ruedas
    #2coche= ruedas - 2vehiculo --> coche=(ruedas-2vehiculo)/2 --> coche= rueda/2 -vehiculo
def cochesYmotos(vehiculos,ruedas):
    coche= ruedas/2 -vehiculos
    moto= vehiculos - coche #Ya no hace falta el IF porque estoy comprobando con "arrastrar" el valor de coche
    return int(coche), int(moto)
print(cochesYmotos(6,20)) #Redujimos las operaciones a 1 sóla (2 operaciones)
#O(1) -- Constante



