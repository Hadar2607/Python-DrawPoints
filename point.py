# -*- coding: utf-8 -*-
"""
Created on Thu Jul 22 10:29:39 2021

@author: hadar
"""
import math

class point:
    
    def __init__(self,x,y):  # constractor Initializes two points
        self.__x=x
        self.__y=y
        
    def get_x(self):     # func that return x value because is private (getter)
        return self.__x  
    
    def get_y(self):     # func that return y value beacuse is private (getter)
        return self.__y
    
    def distance(self,other): # return distance between two points
        return math.dist([self.__x,self.__y],[other.__x,other.__y])
        

    def midPoint(self,other):  # return midpoint between two points
        return point((self.__x+other.__x)/2, (self.__y+other.__y)/2)


    def __str__(self): # override str method
        return "({},{})".format(self.__x,self.__y);

        
        



        
        
        
        
        

