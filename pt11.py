'''ques 3'''
var= int(input("enter a year:"))
if var%4==0 :
    print("it is a leap year")
elif var%400==0 : 
    print("leap year")
 
else:
 print("not a leap year")