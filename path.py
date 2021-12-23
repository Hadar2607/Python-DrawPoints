# -*- coding: utf-8 -*-
"""
Created on Thu Jul 22 14:59:31 2021

@author: hadar
"""
import math
from point import point
from pathIt import pathIt
import random

class path:
    
    
    
    def __init__(self): # constractor that Initializes list type of point  

        self.__round = []
        
    def get_Round(self):     # func that return round list  because is private (getter)
        return self.__round
    
    def fillRandom(self,start,end,size): # create random list
        randList  = [random.randint(start,end) for x in range(size*2)]
        self.fill(randList)
      
    def fill(self,listpoints): # Function that receives list and, make pair of point 
       it = iter(listpoints)
       for x in it:
           self.__round.append(point(x,next(it)))
               
    def __str__(self):  
        x=""
        for i in self.__round:
            x+=str(i)
        return x
                                   
    def merge(self,otherPath): # merge 2 list
        self.__round+=otherPath.__round

                      
    def __iter__(self): #override iter func
        return pathIt(self)
        
        
        
        
    
            
        
        
                        
    
    
    
    
    
    
    
    
    
                                  
        
        
        

        
        
            
            
            
        
        
        
        
        
        
        
