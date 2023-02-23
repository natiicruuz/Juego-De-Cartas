#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 08:51:32 2022

@author: naticruz
"""
import cartas
import resultados
import random
import datetime as dt


nombreUser = input ("Por favor ingrese su nombre:")
print (f"Hola, {nombreUser} !")

print("-----------------------------------")
print("Elija la opcion deseada:")
print("1. Iniciar Juego")
print("2. Ver Puntuaciones")
print("3. Salir")
print("-----------------------------------")



op = input("Opcion:")

if op == "1":
    print("Iniciar Juego")
    print("<------------------------------------------------>")
    print ("Bienvendo/a al juego de cartas")  
    print (" ")
    
    
    mazo = cartas.crear_mazo()
    mazo_revuelto = cartas.revolver_mazo(mazo)
    tuplaYbaraja = cartas.sacar_cartas(mazo_revuelto,numEntero = 10)
    cartaPlayer = tuplaYbaraja[0]
    cartaCompu = tuplaYbaraja[1][11:21]
 
    palos = ["Corazones", "Diamantes", "Treboles", "Picas"]
    fuerte = random.choice(palos)
    print("palo fuerte: ",fuerte)
    debil = random.choice(palos)
    if debil == fuerte:
        debil = random.choice(palos)
    print("palo debil: ",debil)
    print (" ")
    

    print("Tus cartas: ")
    for cart in cartaPlayer:
        cart.imprimirCarta()
        
    print (" ")
    
    
    apuesta = int(input("indique el numero de encuentros que cree ganar(entre 1 y 10)"))
     
    print(" ------------------------------------------------------------------------")
   
    user_point = 0 
    compu_point = 0
    
    for x in range(0,10):
        cartaPlayer[x].imprimirCarta(),cartaCompu[x].imprimirCarta()
        
        #Mismo palo fuerte-debiles
        if cartaPlayer[x].palo == cartaCompu[x].palo: 
            
            if cartaPlayer[x].num > cartaCompu[x].num:
                user_point+=1
                print("Ganaste un punto. Llevas",user_point,"puntos")
                
            elif cartaPlayer[x].num < cartaCompu[x].num:
                compu_point+=1
                print("No ganaste un punto.")
                print("El oponente lleva",compu_point,"puntos")
                
            elif cartaPlayer[x].num == cartaCompu[x].num: 
                user_point+=1
                print("Tienen el mismo numero, punto a favor tuyo! Llevas",user_point,"puntos")
         
        #Mismo palo regulares      
        elif ((cartaPlayer[x].palo != fuerte and debil) and (cartaCompu[x].palo != fuerte and debil)):
            
            if cartaPlayer[x].num > cartaCompu[x].num:
                user_point+=1
                print("Ganaste un punto. Llevas",user_point,"puntos")
                
            elif cartaPlayer[x].num < cartaCompu[x].num:
                compu_point+=1
                print("No ganaste un punto.")
                print("El oponente lleva",compu_point,"puntos")
                
            elif cartaPlayer[x].num == cartaCompu[x].num: 
                user_point+=1
                print("Tienen el mismo numero, punto a favor tuyo! Llevas",user_point,"puntos")
            
                
        #mi carta es fuerte y la compu tiene debil       
        elif ((cartaPlayer[x].palo == fuerte) and (cartaCompu[x].palo != debil)): 
            user_point+=1
            print("Ganaste un punto. Llevas",user_point,"puntos")
            
            
        #La carta de la compu es fuerte y la mia es debil
        elif ((cartaCompu[x].palo == fuerte) and (cartaPlayer[x].palo != debil)):
            compu_point+=1
            print("No ganaste un punto.")
            print("El oponente lleva",compu_point,"puntos")
            
            
        #mi carta es regular y la de la compu es debil    
        elif ((cartaPlayer[x].palo != fuerte and debil) and (cartaCompu[x].palo == debil)):
            user_point+=1
            print("Ganaste un punto. Llevas",user_point,"puntos")
            
            
        #la carta de la compu es regular y la mia debil
        elif ((cartaCompu[x].palo != fuerte and debil) and (cartaPlayer[x].palo == debil)):
            compu_point+=1
            print("No ganaste un punto.")
            print("El oponente lleva",compu_point,"puntos")
            
            
        #Mi carta es debil y la de la compu es fuerte    
        elif ((cartaPlayer[x].palo == debil) and (cartaCompu[x].palo == fuerte)):
            user_point+=1
            print("Ganaste un punto. Llevas",user_point,"puntos")
            
            
       #Mi carta es fuerte y la de la compu debil 
        elif ((cartaPlayer[x].palo == fuerte) and (cartaCompu[x].palo == debil)):
            compu_point+=1
            print("No ganaste un punto.")
            print("El oponente lleva",compu_point,"puntos")
            
        
        print(" ")
        
    puntos = 10-(abs(user_point - apuesta))
    print("Tus puntos en esta partida fueron: ", puntos)
    
    
    fecha = dt.datetime.now()
    formato = "%Y/%m/%d %H:%M"
    
    dato = resultados.Resultado(fecha.strftime(formato), nombreUser, puntos)

    #vieja info
    viejo = resultados.cargar_resultados()
    #agregar nuevo resultado
    lista = []
    lista.append(viejo)
    
    lista.append(dato.imprimirInfo())
   
    resultados.guardar_resultados(lista)
    

        
        
    print("=====================================================================")   
    print("Gracias por jugar :) ")
    
elif op == "2":
    print("Resultados")
    print("<------------------------------------------------>")
    print ("Bienvendo/a a los resultados!")  
    print (" ")
    
    print("Resultados....")
    print(resultados.cargar_resultados())
    
  
elif op == "3":
    print("Gracias por Jugar!")
    exit()
    
else:
    print("opcion invalida")
    

