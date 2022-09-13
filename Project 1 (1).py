#!/usr/bin/env python
# coding: utf-8
####  MUBEENA WAHAJ
#### PROJECT 1

#Things to do in the program:
## 1.Input
##       Receive the coefficients (A, B, C) individually and interactively from the keyboard with a specific prompt message              specifying the coefficient being received.
## 2.Calculate the roots (two roots)
## 3.Output 
##     o Display coefficient A
##     o Display coefficient B
##     o Display coefficient C
##     o Display the roots


# In[36]:


# Getting our inputs

A = float(input('Enter value for coefficient A: '))
B = float(input('Enter value for coefficient B: '))
C = float(input('Enter value for coefficient C: '))

#Quadratic Calculation 

inside_calculations = (B ** 2)-(4 * A * C)      
Root_1 = (-B + (inside_calculations**0.5) )/ (2 * A) #first approach: done so that calculation does 
                                                                            #not get too complicated


Root_2 = (-B - (((B ** 2)-(4 * A * C) )** 0.5)) / (2 * A)   #second approach

#Outputting our values
print('\n Your coefficient A value is:',A,'\n Your coefficient B value is:', B,'\n Your coefficient C value is:' , C )
print (' Your Root values are:', Root_1 , 'and ', Root_2)

