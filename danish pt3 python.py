#!/usr/bin/env python
# coding: utf-8

# In[22]:


'''NAME :- SYED DANISH ALI ; ROLL NO :- 2K18CSUN01043 ; PT3-PYTHON'''

#Theoretical Questions:


#Q1.What is the syntax to call a constructor of a base class from child class?

#ANS 1. we can call using super() Command.
''''
class A(object):
     def _init_(self):
        print("world")

class B(A):
       def _init_(self):
        print("hello")
        super(B, self)._init_()
B()
'''

    
#Q2.How is a class made as inherited class (syntax of child class) ?

#ANS 2. 
'''
class Parent:
     pass
class Child(Parent):
     pass
'''
#Q3.Print an element of a nested dictionary ?
'''
people = {1: {'name': 'DANISH', 'age': '20', 'sex': 'Male'},
          2: {'name': 'HARSHITA ','age': '20', 'sex': 'Female'}}

print(people[2]['name'])
print(people[2]['age'])
print(people[2]['sex'])
'''


# In[1]:


#Programming Questions-     SET - C

#Q2.Please write a program which accepts a string from console and print the characters that have even indexes.

print("Please enter text to print::")
inputchars = input()

if inputchars:
    string = ""
    for i in inputchars:
        if inputchars.index(i)%2 == 0:
            string += str(i)
    
    print('-------------------')
    print("You Entered:", inputchars)
    print("Result:")
    print(string)


# In[ ]:


#Q1.Write a program that calculates and prints the value according to the formula given below. Take three values from user. Q= square root (( 2*value1*value2)/value3) ?

print("enter value 1")
value1=int(input())
print("value2")
value2=int(input())
print("value3")
value3=int(input())
q=(((2*value1*value2)/value3))**0.5
print("result is"+ str(q))


# In[ ]:




