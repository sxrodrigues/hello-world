#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 15:45:24 2019

@author: serenerodrigues
"""

class person(object):
    def __init__(self,name,age,height):
        self.name = name
        self.age = age
        self.height = height
        
    def printprofile(self):
        print(self.name, self.age, self.height)


class student(person): #class - functions with variables grouped into a class
    def __init__(self,marks,name,age,ID,height=150): 
        self.marks = marks
        self.ID = ID
        person.__init__(self,name,age, height)

    def average(self):
        s = 0.0
        for mark in self.marks:
            s += mark
        return s/len(self.marks)
            
        
student1 = student([90,40,100],"Iain", 19, 985) 
student2 = student([100,100,100,100],"Serene", 19, 986)

print(student1.printprofile())
(student2.average())