#while loop 
c=1
while (c <=10):
   print("....HELLO WORLD....")
   c+=1
   
#single line while loop
cnt=0
while(cnt==0): print("....HELLO GREEK....") ; break
#without break , loop run infinitely 

#for loop example 1
print("....list iteration....")
list=['geeks' , 'for' , 'geeks']
for i in list:
   print(i)

#for loop example 2 => iterating over tuple (immutable)
print("\n ....Tuple iteration....")
t=('geeks' , 'for' , 'geeks')
for i in t:
   print(i)

#for loop example 3 => iterating over a string
print("\n ....String Iteration....")
s="Geeks"
for i in s:
   print(i)
   
#iterating by index of sequences
#iterating by index
print("\n....Iterating by index of sequence....")
listt=['Geeks' , 'For' , 'Geeks']
for index in range(len(listt)):
    print(listt[index])
    
#Loop Control statements....

#continue statement is used in loopps when programmer want to skip the current iteration
#print all letters except 'e' and 's'
print("\n....Continue statement....")
for letter in 'geeksforgeeks':
   if letter == 'e' or letter == 's':
      continue
   print("Current Letter => " , letter)
   
#break statement => is used to move control out of the loop
print("\n....Break statement....")
for letter in 'geeksforgeeks':
   if letter == 'e' or letter == 's':
      break
   print("Current Letter => " , letter)

#Python Function
#creating a function
print("\n....Create function....")
def myfun():
   print("Hello from the function....")
#calling a fuvntion
print("\n....Calling Function....")
myfun()
#parameters....
print("\n....Parameters in function...")
def myfunc(fname):
   print(fname + "Refsnes")
   
myfunc("Emil")
myfunc("Tobies")
myfunc("Linuss")

#default parameters.....
print("\n....Default Function....")

def mefunction(country="Norway"):
   print("I am from " + country)   
mefunction("Swedan")   
mefunction("Pakistaaan")   
mefunction("Indiaaa")

#passing a list as a parameter...
print("\n....passing a list as a parameter....")
def myfu(food):
   for x in food:
      print(x)
      
fruits=["banana " , 'mango' , 'apple' , 'strawberry' , 'guava']
myfu(fruits)

#Return Values....
print("\n ....Returning value....")
def my_func(x):
   return 5*x
print(my_func(5))
print(my_func(7))
print(my_func(6))

#keyword arguments with key=value
print("\n ....Key=value entering....")
def myfunct(child3,child2,child1):
   print("The Youngest child is " +child3)
   
myfunct(child1="Emiul" , child2="Tabious" , child3="Linus")

#Python classes / objects
#Create a class....
print("\n ....Creating class....")
class myclass: x=5
#create a object....
p1=myclass()
print("\n ....print object after creating....")
print(p1.x)

#init() function
#it is used to assign values to the object properties 
#or other operations that are necessary to do when the obj is being created
 
""" create a person class , use init() function to assign values
for the age and name"""
print("\n ....init function()....")
class person:
    def __init__(self,name,age):
       self.name=name
       self.age=age
             
p=person("john" , 36)   
print(p.name)
print(p.age)

# object methods
class person:
    def __init__(self,name,age):
         self.name=name
         self.age=age
    def myf(self):
        print("Hello my name is " + self.name )
        print("I am ",self.age ," Years oold")

p=person("john" , 18)
print(p.name)


