print ("Hello World from .py file.")
x = 1
x = "ABC"                                                   #variable mapping
print (x)

numbers = [1,2,3,4,5,6,7,8,9,10]                            #list
sixth = numbers[5]
print (sixth)

purchase = {"apple" : "1Kg" , "orange" : "2Kg"}             #dictionary
weight = purchase["orange"]
print (weight)

present = True
absent = False
message = None              #empty object

if present == True:
    print ("Good")
elif present == False:
    print ("False Statement")
else:
    print ("Bad")           #if None

for x in numbers:
    print (x)


def skip():               #function without content runs by pass
    pass
def addition(a,b):           #function needs content
    print ("Hello")
    return (a+b)

add = addition(10,15)
print (add)

class MyStudent:               #Camel Casing
    first_name = "Aditya"



