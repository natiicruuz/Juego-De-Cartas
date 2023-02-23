#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 13 19:57:50 2022

@author: naticruz
"""

import pickle

class Resultado:
    
    def __init__(self,fecha,user,puntos):
        self.fecha = fecha
        self.user = user
        self.pts = puntos
        
    def imprimirInfo (self):
        resultado = "fecha:", self.fecha,"jugador:", self.user, "Puntos:", self.pts
        return resultado
      
def guardar_resultados(lista_de_objetos_resultado):
    
   
    with open("resultados.pickle", "wb") as archivo:
 
        pickle.dump(lista_de_objetos_resultado,archivo)
        
      
def cargar_resultados():
    
    with open("resultados.pickle", "rb") as archivo:
        load = pickle.load(archivo)
        return load
       
        
        
      
    


