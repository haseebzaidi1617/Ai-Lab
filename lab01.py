#task 1
#First task is the commenting ... this is the single line comment 
"""This is the multiline commenting
My name is syed haseeb abbas zaidi
My father name is syed qaiser abbas zaidi"""

print("HELLO WORLD") #displaying text
#task 2
str=int(input("Ener your Age : ")) #input
print("My age is : " , str) #output
#task 3
#multiple statements printing
print("Artificial Intelligence \n Analysus of Algorithms") # 1st type
#2nd type
print("Artificial Intelligence")
print("Analysis of Algo") 
#3rd type
print("Artificial Intelligence") ; print("Analysis of Algorithmss")
#task 4
#indentation is mendatory
x=2
if(x>5):
#print("yess dear") this is the issue bkz here this is no indexing
   print("HEllo zaidi sahib")
#task 5  
#checking the type of variable
str="Haseeb abbas"
x=3
y=33.34
xy=True
print(type(xy))
print(type(x))
print(type(str))
print(type(y))

#writing complex numbers
x=complex(3,4)
print(x)
print(type(x))
#task 6
#special characters in strings
# \n \t \\ \' \"
print("Haseeb abbas \nQaiser Abbas")
print( " Haseeb Abbas is the son of \"Syed Qaiser Abbas\" Resident of District Wzd")
print("Haseeb abbas \t Qaiser Abbas")

#task 7
 #indexing
str12="Muhammad Mustafa"
print(str12[7])
print(str12[-3])

#task 8
#slicing
print(str12[0:8])
print(str12[:6])

#task 9
#list creating
mylist=[12,13,14,15,16,17]
print(mylist)
print(mylist[2])
list2=['black','brown','green','yellow']
print(list2)
print(list2[3])
list3=[23.2,45,'voilet','$']
print(list3[2])

#task 10
#conditional statements
xx=99
if(xx>=90 and xx<=100):
   print("....EXCELLENT BOYY....")
elif(xx>=80 and xx<=89):
   print("....VERY GOOD....")   
elif(xx>=70 and xx<=79):
   print("....GOOD....")
elif(xx>=50 and xx<=69):
   print("....FAIR RESULT....")
else:
   print("FAIL .... TRY AGAIN ")