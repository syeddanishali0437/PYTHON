#!/usr/bin/env python
# coding: utf-8



### GIT HUB URL ::::---  https://github.com/DanishAli-MRU/PYTHON.git  ; GIT HUB USER NAME : :- " DanishAli-MRU " ; danishali0437@gmail.com ;

''' FULL LAB FROM JAN TO MAY '''


# In[1]:


#Lab2

#Q1

n=int(input("Enter Number:"))

if n%2==0:
    print("Number",n,"is Even")
else:
    print("Number",n,"is Odd")


# In[2]:


#Q2

n=int(input("Enter a YEAR:"))

if n%4==0:
    if n%100==0:
        if n%400==0:
            print("LEAP YEAR")
    else:
        print("NON Leap Year")

else:
    print("NON Leap Year")


# In[3]:


#Q3

str=input("Enter a Character:")

if str=='a' or str=='e' or str=='i' or str=='o' or str=='u':
    print(str,"is a Vowel")
else:
    print(str,"is Non-Vowel")


# In[4]:


#Q4

n=int(input("Enter First Number:"))
n1=int(input("Enter Second Number:"))

if n>n1:
    print("1st Number is Greater")
else:
    print("2nd Number is Greater")


# In[5]:


#Q5

n=int(input("Enter Number for Factorial:"))

for i in range(1,n):
    i=i*n
    
print("Factorial of Number is:",i)


# In[6]:


#Q8

n=int(input("Enter a Number:"))

for i in range(2,n):
    if n%i==0:
        print(n,"is a Non-Prime Number")
        break
    if n%i!=0:
        print(n,"is a Prime Number")
        break


# In[ ]:


#Q10

def sum(x,y):
    return x+y
def product(x,y):
    return x*y
def fact(x):
    fact=1
    i=1
    for i in range(1,x+1):
        fact=fact*i
    return fact

def diff(x,y):
    if x>y:
        return x-y
    else:
        return y-x

def div(x,y):
    return float(x/y)

def lcm(x,y):
    if x>y:
        z=z
    else:
        z=y

    while True:
        if z%x==0 and z%y==0:
            lcm=z
            break
        z=z+1
    return lcm



    
p=int(input("Enter Password"))
if p==1112:
    print("1.SUM")
    print("2.PRODUCT")
    print("3.FACTORIAL")
    print("4.DIFFERENCE")
    print("5.DIVIDE")
    print("6.LCM")
    
    n=int(input("Enter Your Choice"))
    if n==1:
        a=int(input("Enter First Number:"))
        b=int(input("Enter Second Number:"))
        print("Sum is",sum(a,b))
    elif n==2:
        a=int(input("Enter First Number:"))
        b=int(input("Enter Second Number:"))
        print("Sum is",product(a,b))
    elif n==3:
        a=int(input("Enter Number:"))
        print("Factorial is",fact(a))
    elif n==4:
        a=int(input("Enter First Number:"))
        b=int(input("Enter Second Number:"))
        print("Difference is",diff(a,b))
    elif n==5:
        a=int(input("Enter First Number:"))
        b=int(input("Enter Second Number:"))
        print("Division is",div(a,b))

    elif n==6:
        a=int(input("Enter First Number:"))
        b=int(input("Enter Second Number:"))
        print("LCM is",lcm(a,b))
else:
    print("Invalid Password")
        


# In[ ]:





# In[ ]:


#Lab3

#Q2.Print 1st 5 even numbers (use break statement).

n=int(input("Enter Range:"))
for i in range(1,n):
    if i%2==0:
        print(i)
    if i%2!=0:
        continue


# In[ ]:


#Q3.Print 1st 4 even numbers (use continue statement).

n=int(input("Enter Range:"))

for i in range(1,n):
    if i%2==0:
        print(i)
    if i%2!=0:
        continue


# In[ ]:


#Q5.Write a Python program to calculate the length of a string.
A="Hello"
count=0
for i in A:
    count=count+1
print(count)


# In[ ]:


#Q6.Write a Python program to count the number of characters (character frequency) in a string

A="Manav Rachna University"
count=0
for i in A:
    if i=='a':
        count=count+1
        
print("Number of A in String is",count)


# In[ ]:


#Q7.Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. If the string length is less than 2, return instead of the empty string.

str=input("Enter a String:")
len=len(str)

if len<=2:
    print("Not Valid")
else:
    print(str[0]+str[1]+str[count-2]+str[count-1])


# In[ ]:


#Q8.Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself#

str=input("Enter a String:")

a=str[0]

str1=str.replace(a,"$")

print("Final String is",a+str1[1:])        


# In[ ]:


#Q9.Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string. 

str=input("Enter First String:")
str1=input("Enter Second String:")

a=str+" "+str1
print("Total String is",a)

b=str.replace(str[0],str1[0])
c=str1.replace(str1[0],str[0])

print("Final String after Replacement is",b+' '+c)


# In[ ]:


#Q10.Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing' then add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged

str=input("Enter a String:")
str1=""

if len(str)<3:
    print("No Change")
else:
    if str[-3:]=='ing':
        str1=str+'ly'
    else:
        str1=str+'ing'
    
print(str1)


# In[ ]:





# In[ ]:


#Lab-4-5

#Q1
a=("Hi")


# In[ ]:


#Q2
a=("Hi",2,2.3)
print(a)


# In[ ]:


#Q3

a=(1,3,4,12)
print(a[0])


# In[ ]:


#Q5

a=(1,4,5,12,34)
x=int(input("Enter Number to add in the Tuple:"))

a=a+(x,)

print(a)


# In[ ]:


#Q6

tup=("Hi","Brother")
str=''.join(tup)
print(str)


# In[ ]:


#Q7

tup=(1,2,3,4,5,6,7,8,9,10)
print(tup[3])


# In[ ]:


#Q9

tup=(1,2,3,4,1)
a=tup[0]
for i in tup:
    if i==a:
        print("Element",a,"found")
    else:
        continue


# In[ ]:


#Q10

tup=(1,2,3,4,5)
x=int(input("Enter a Number:"))

for i in tup:
    if i==x:
        print("Yes",x,"is present")
    else:
        continue


# In[ ]:


#Q11

list=[1,1,2,3]
tup=tuple(list)
print(tup)


# In[ ]:


#Q12

tup=(1,100,123,4,34,78,98)
tup=tup[:3]+tup[4:]
print(tup)


# In[ ]:


#Q13

tup=(3,5,1,100,45,12,65)
tup=tup[:2]+tup[3:]
print(tup)


# In[ ]:


#Q14

tup=(2,5,12)
x=int(input("Enter Number to find Index:"))

for i in tup:
    if i==x:
        print("Number",x,"found at",i-1,"location")
        
    else:
        continue


# In[ ]:


#Q15

tup=(12,3,45,12)
sum=0
for i in tup:
    sum=sum+1
print("There are",sum,"elements")


# In[ ]:


#Lists-Q1

a=[1,2,3,4]
print(sum(a))


# In[ ]:


#lists-Q2

li=[1,2,3,4]
mul=1
for i in li:
    mul=mul*i
print("Multiplication is",mul)


# In[ ]:


#Lists-Q3

a=[1,100,45,12,15]
print("Maximum from list is",max(a))


# In[ ]:


#Lists-Q4

a=[10,100,34,100]
print("Minimum is",min(a))


# In[ ]:


#lists-Q5

a=["1221","aba","abc","xyz","ana"]
sum=0
for i in a:
    if i[0]==i[-1]:
        sum=sum+1
        
print(sum)


# In[ ]:


#Lists-Q7

k=[]
a=[1,2,3,1,9]
for i in a:
    if i not in k:
        k.append(i)
            
print(k)
            


# In[ ]:


#Lists-Q8

a=[]
if len(a)>0:
    print("List is Not Empty")
else:
    print("List is Empty")


# In[ ]:


#Lists-Q9

a=[1,2,3]
b=[]

for i in a:
    b.append(i)
print(b)


# In[ ]:


a=["Hello","Hi","Halwa","Ayush","AK"]
b=[]
count=0
for i in a:
    for j in i:
        count=count+1
    if count>2:
        b.append(i)
    count=0

print(b)
    
    


# In[ ]:


def common(list1, list2):
     
     for x in list1:
         for y in list2:
             if x == y:
                 result = True
                 return result
print(common([1,2,3,4,5], [5,6,7,8,9]))


# In[ ]:


a=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow',"Hello","Hi",1,2]
a.remove(a[0])
a.remove(a[4])
a.remove(a[5])
print(a)


# In[ ]:





# In[ ]:


#Lab-7

def mul(x,y):
    return x*y

x=2
y=3
print("Multiplication is",mul(x,y))
    


# In[ ]:


def add(x,y):
    return x+y

x=2
y=7
print("Addition is",add(x,y))


# In[ ]:


def fact(x):
    fact=1
    for i in range(1,x+1):
        fact=fact*i
    return fact

print("Factorial is",fact(3))


# In[ ]:




def Fibonacci(n): 
    if n<0: 
        print("Incorrect input") 
    elif n==1: 
        return 0
    elif n==2: 
        return 1
    else: 
        return Fibonacci(n-1)+Fibonacci(n-2) 


print(Fibonacci(9)) 


# In[ ]:


def swap(x,y):
    temp=x
    x=y
    y=temp
    return x,y

print("Numbers Swapped",swap(2,3))


# In[ ]:



def gcd(a,b): 

 
    if (a == 0): 
        return b 
    if (b == 0): 
        return a  
    if (a == b): 
        return a 
 
    if (a > b): 
        return gcd(a-b, b) 
    return gcd(a, b-a) 

 
a = 92
b = 55
if(gcd(a, b)): 
    print('GCD of', a, 'and', b, 'is', gcd(a, b)) 
else: 
    print('not found') 


# In[ ]:


c=input("Enter a Character")
print("The ASCII value of '" + c + "' is", ord(c))


# In[ ]:


import datetime
from datetime import date

print ("Present date is : ") 
print (date.today()) 


# In[ ]:


def greet(name,message):
    print("Hello",name,".",message)
    
greet("AK","How Are You?")


# In[ ]:


def greet(name,message="How Are You?"):
    print("Hi",name+message)
greet("AK")
greet("How do you do?")


# In[ ]:





# In[ ]:


#Lab-9

class Triangle:
    a=3
    b=4
    def create_triangle():
        return print("Triangle is created")
        
    def print_sides(a,b):
        return print("Sides are",a,"and",b)
        
a=2
b=3
print(Triangle.create_triangle())

print(Triangle.print_sides(a,b))
    


# In[ ]:


class string:
    def inputstr():
        str=input("Enter a string")
        
    def printstr(str):
        return str
    
    
string.inputstr()
print(string.printstr(str))
        


# In[ ]:


class Rectangle:
    
    def perimeter(length,breadth):
        per=2*(length+breadth)
        return per
    
print("Perimeter is",Rectangle.perimeter(2,3))


# In[ ]:


class Circle:
    
    def area(r):
        area=3.14*r*r
        return area
    
    def perimeter(r):
        per=2*3.14*r
        return per
    
    
print("Area of circle is",Circle.area(2))
print("Perimeter of circle is",Circle.perimeter(3))
        


# In[ ]:




class Class1: 
    def m(self): 
        print("In Class1") 

class Class2(Class1): 
    def m(self): 
        print("In Class2") 

class Class3(Class1): 
    def m(self): 
        print("In Class3") 

class Class4(Class2, Class3): 
    pass

obj = Class4() 
obj.m() 


# In[ ]:





# In[ ]:


#Lab10

class Animal:
  def _init_(self, leg):
    self.leg = leg

  def printleg(self):
    print(self.leg)

class tiger:
    x = Animal("4")
    print("Tiger has leg:- ", end="")
    x.printleg()
class dog:
    x = Animal("4")
    print("Dog has leg:- ", end="")
    x.printleg()


# In[ ]:


class Employee:
  def _init_(self, desg):
    self.desg = desg

  def printdesg(self):
    print(self.desg)

class engineer:
    x = Employee("Enginner")
    print("This has a designation of:- ", end="")
    x.printdesg()
class manager:
    x = Employee("Manager")
    print("This has a designation of:- ", end="")
    x.printdesg()


# In[ ]:



class MyClass:
    "This is my second class"
    a = 10
    def func(self):
        print('Hello')
print(MyClass.a)
print(MyClass.func)
print(MyClass._doc_)


# In[ ]:


class Parent(): 
    def _init_(self): 
        self.value = "Inside Parent" 
    def show(self): 
        print(self.value) 
class Child(Parent): 
    def _init_(self): 
        self.value = "Inside Child"
    def show(self): 
        print(self.value)  
obj1 = Parent() 
obj2 = Child() 
  
obj1.show() 
obj2.show() 


# In[ ]:



class Class1: 
    def m(self): 
        print("In Class1")  
class Class2(Class1): 
    def m(self): 
        print("In Class2") 
class Class3(Class1): 
    def m(self): 
         print("In Class3")      
class Class4(Class2, Class3): 
    def m(self): 
        print("In Class4")    
obj = Class4() 
obj.m() 
  
Class2.m(obj) 
Class3.m(obj) 
Class1.m(obj)
