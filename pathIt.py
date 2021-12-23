# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 11:31:28 2021

@author: hadar
"""



class pathIt:
    
      def __init__(self, path):
          self.path = path
          self._it = iter(path.get_Round())
                  
      def __next__(self):
          return next(self._it)
    
    
      def __iter__(self):
          return self



