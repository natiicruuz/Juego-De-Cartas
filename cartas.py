#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 16:27:16 2022

@author: naticruz
"""
import random 


class Carta:
    def __init__ (self,numeroCartas ,palo):
        self.num = numeroCartas
        self.palo = palo
       
        
    def imprimirCarta (self):
        print(self.num,"de", self.palo)
     

        
def crear_mazo():
    mazo_completo = []
    numeros = {1:"As", 2:"2", 3:"3", 4:"4", 5:"5", 6:"6", 7:"7",8:"8", 9:"9", 10:"10", 11:"J", 12:"Q", 13:"K"}
        
    for n in ["Corazones", "Diamantes", "Treboles", "Picas"]:
        for v in numeros.values():
            mazo_completo.append(Carta(v,n))
           
    
    return mazo_completo


mazo = crear_mazo()



def revolver_mazo(mazo):
    random.shuffle(mazo)
    return mazo

   
mazo_revuelto = revolver_mazo(mazo)

def sacar_cartas(mazo_revuelto,numEntero = 10):
    
    barajaPlayer = list(mazo_revuelto[0:10])
    resto = mazo_revuelto[10:52]
    
    tupla = (barajaPlayer,resto)
    return tupla









