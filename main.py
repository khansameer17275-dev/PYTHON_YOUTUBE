"""Variables"""

# sher = "Rohit Bhaiyya"

# SheryianSchool = "students" #pascal case

# sheryianSchool = "students" #camel case

# sheryians_school = "students" #snake case

# a = 12 #data types integers

# print(type(a))

# a = -34 # data types integers

# b = 56.8 # data types float
# c = 12/3 # data types float

# v = 34j  # data types complex

# print(type(v))



# st = '1234512345 asdfghjkl !@#$%^'

# print(type(st)) # data types strings any type of key in keyboard is strings.

# b = True # data types is boolean starting T & F are capital

# t = False # also  boolean 

# print(type(t))

"""Strings"""

# a = "A"
# print(ord(a)) # har ek jo character numbers value hoti hai strings ki uska unicode hota hai.
              #ord unicode me convert krta hai character ko.

# a = 65

# print(chr(a))# chr unicode ko character me convert krta hai. strings ka thoda jyada space rahta hai.

# a = "SHER" #S-0 H-1 E-2 R-3 strings indexing me 0 se count hota hai isse mai koi bhi beech ka alphabet print kara sakta hoo.

# print(a[1])

# a = "SHER" # mai agar -1 krta hoo to bhi R print hoga aur 3 krta hoo to R hoga

# print(a[-1],a[3])

#string slicing 
#koi badi strings hai usko kisi hisse ko slice krke nikal na

# a = "SHER CODER"

# print(a[0:4:1])# ye sqaure box me first value start second stop third step R-3 tha par ek kam print hota hai islie 4.


# print(a[5::])# coder print hua

# print(a[6:9:])#ODE print karaya o ki value 6, e ki 8 hai lekin ek jyada lete h stop me


#Type Conversion- there are more function but these are 4 main function looking at these function these are used to convert one data to another. int,float, str,bool
# paranthesies are also  function

# a = 12 

# a = str(a)# conversion integers to strings

# print(a)

# a ="12"

# a = int(a)

# print(type(a))#dhyan rakhna integer conversion hai numbers hi honge convert.

# a = 12

# print(bool(a))#Falsi value 7 values hai jab false print hoga boolean conversion me.
#1-False 2-0 3-0.0 4-"" 5-[] 6-() 7-{} inme false aaega baaki saari true aaengi


# implicit mtlb python automatically convert krta hai

# a = 12

# print(12/3)#iska answer dega float implicit apne aap krta hai

# input and output in python

# name = "Sameer"
# age = "21"

# print("Hello my name is",name,"and my age is",age) # one way of writing

# print(f"my name is {name} and my age is {age}") #formatted strings hai ye 

# age = int(input("hello what is your age")) #user input kaise lete h terminal me aata hai

# print(age)# int likhne se output to same hai bas integer hi aaega 

# number = input("Accept numbers from a user")

# print(number)

"""Arithmetic Operations"""
# Operators are symbol that perform operations on variables and values. Python has several types of 
#operators for different task like arithmetic,comparision logical operations

#Arithmetic operators perform mathematical opetrations like addition, substraction,multiplication,division,etc
#there are 7 types of arithmtic operator 
# 1-addition 2-substraction 3-multiplication 4-division 5-floor division-// 6-modulus-% 7-exponentiation

a = 5
b = 32 

# print(a + b) #addition
# print(b - a)#substraction
# print(a * b)#multiplication
# print(b / a)#division
# print(b // a)#floatdivision isme decimal ke baad wali value show nai hoti
#print(5**5)#exponential operation square of the value.
#print(32%5)#mode operation me remainder aata hai 

#print(12+4/2)#bodmass rule firstly divide multiply add substract

"""Assignmet Operators"""
# Assignment operators are used to assign values to variables python also provide compound assignment operators 
# perform operations like ADD SUB MULTIPLY, ETC
# basics assign oper = isequal to 

#compound assignment operators
  
# a = 20

# a += 20
# a += 40 #ye sab compound assignment hai 
# a += 60
# a -= 10
# a *= 3
# a/= 5
# a//= 2
# a**= 2
# print(a)

# Comparision Operator
# 6 types of omparision operator >,<,>=,<=,==,!=

a = 12.1
b = 12 

# print(a == b) #a is equal to b == iska matlb equal too hai

# print(a != b)#iska mtlb a ke barabar na ho different ho

# print(a > b)

# print(45 < 67)#67 is greater than 45 yes true 
# print(23 > 23)

# print(23 >= 23)
# print(45 <= 45)#hamesha ansswer true ya false aaega kyuki boolean answer dega

#kya ham strings value me kr skte hai kya 

# print(ord("A"))
# print(ord("B"))

#print("ABC" > "ACD")# how to perform operators in strings

#kya mai strings ko number se compare krsaktaa hoo

#print("A" > 34)#cannot perform between strings and integers only perform strings to strings and no to no

#Logical operators
# you are doing one comaparision going on other comparision are perform
#there are three types of logical operators And returns true if both condition are true 
#print(123 > 100 and 34 == 34 and 45 < 90 and 12 > 20) # and operators do what two comparision is true show only once i add both comparision and oper ka funda hai ek bhi false to result false 
#  OR- return True if at least one condition is true
# Not- reverse the boolean value 

#print(12 != 12 or 23 == 45 or 67 == 56 or 10 > 5)#OR bolta hai koi ek bhi true krdo aap 4-5 ya uusse jyada hai agar ek bhi true hai to chalega

#print(not 12 == 12)#NOT operation agar true hai to false aaega mtlb opposite chalta hai

# practice question

#answer true and false
# print(126 > 130)# this is false because 126 is small

# print((456 == 456) != (235 == 236))#first is true second comparision is false third is True  
# print(12 < 10 or 45 == 56 or 69 > 70 or 15 != 13)#first is false second is false third is also false fourth is true so the answer is true because this is or comparision
# print(True and bool(0)) # bool is converter in t and f so the 0 is false value answer is false because its and operation

# conditional statements
# . Conditional statement in python allow decision-making by executing different blocks of code based on conditions.
# Decision making can be understood with an example
# if else statements 
# type of conditional statement generally there are 3 types of variation in conditional
#if - Executes if the condition is True
#if-else - Executes if True, another if false
#if-elif-else - Checks multiple condition in sequence
# IF ELSE

# a = 13

# if a > 10:
#     print("i will do task A")# agar true hai to ye wala print hoga 

# else:
#     print("i will do task B")#agar false hai to ye wala hoga 

# a = 6

# if a > 10:
#     print("i will do task A")# agar true hai to ye wala print hoga 

# else:
#     print("i will do task B")#agar false hai to ye wala hoga 

# money = int(input("please provide the money :- "))

# if money == 10:
#     print("I will have a choco bar icecream")

# elif money == 20:
#     print("I will have a mangodolly")

# elif money == 30:
#     print("i will have a frosty")   
# else:
#     print("i will have a cone")

# practice questions


# num1 = int(input("please tell your first number"))
# num2 = int(input("please tell your second number"))

# if num1 > num2:
#     print(f"{num1} is greater than {num2}")

# elif num1 < num2:
#     print(f"{num2} is greater than {num1}")

# else:
#     print(f"{num1} is eqaul to {num2}")

# gen = input("please tell your gender as character (M or F):-")

# if gen == 'M' or gen == 'm':
#     print(f"Good Morning Sir")

# elif gen == 'F' or gen == 'f':
#     print(f"Good Morning Mam")

# else:
#     print("unidentified gender")

# num = int(input("please tell your number :-"))

# if num%2 == 0:
#     print("even number")

# else:
#     print("Odd number")

# name = input("please enter your name : -")
# age = int(input("please enter your age : -"))

# if age >= 18 :
#     print(f"Hello {name} you are eligible to vote")

# else:
#     print(f"Hello {name} you are not eligible to vote")

# year = int(input("tell your year :-"))

# if year %100 == 0 and year %400 == 0:#jo 100 se divisible hai unke lie == 0 wala case 
#     print("Its a leap year")

# elif year %100 != 0 and year %4 == 0:#jo 100 se divisible nai hai unko 4 se check krenge
#     print("Its a leap year")

# else:
#     print("its a normal year")

# t = int(input("Please tell your temperature :-"))

# if t < 0:
#     print("Temperature is Freezing cold")

# elif t >= 0 and t <10:
#     print("Temperature is very cold")

# elif t >= 10 and t <20:
#     print("Temperature is Cold")

# elif t >= 20 and t <30:
#     print("Temperature is Pleasent")

# elif t >= 30 and t < 40:
#     print("Temeperature is Hot")

# else:
#     print("Temperature is Very Hot")

# Loops in python

# Loops in Python allow us to execute a block of code multiple times without rewriting it.

# ok lets do one thing go to your vs code and print hello world 100 times 

# manually printing will take 100 code lines to print it. but using loops we need only two lines to print 100 times that the power of loops.

# types of loops 
# there are two types of loops in python for and while loop.
# for loop me number mtlb kitne baar chalana hai
# while me comditions hoti hai ki kab tak chalana hai kya krna hai true ya false.

#print("Hello World")

# For Loop

#range()# range fun accept 3 things (s,s,s)start, stop, step(1,20,2) 1,3,5,7,9.

# a = range(1,21,1) ham isko directly bhi print kara sakte h

# for i in a:
#     print(i)

#for i in range(21): # mai isme start step number hata kar bhi loop chala sakta hoo.
   # print(i)# ab maine stop  button ke use se bhi print kara dia value 0 se hui print kyuki mai start me khuch ni likha pahle start me 1 likha tha.

#ab mai ulta jaana chahta hoo 16 se 1

#for i in range(16,0,-1):
  #  print(i)

#for i in range(20,51):
   # print(i)

# for i in range(-3,-16,-1): #yaha par islie likha hoo kyukindefault me 1 hai step me islie apan ko conditionn change krna hai.
   # print(i)

#lets print a table of 5

# for i in range(5,51,5):
#     print(i)

#lets print a table of 7

#for i in range(7,71,7):
   # print(i)
# if you try to put by the user.
#n = int(input("Which Table you want ? ")) # agar user ko print krwana hai to aese krna hai

#for i in range(n,(n*10)+1,n):
  #  print(i)

# Loops for strings

# loops for strings work slightly, differently you can iterate through a string in two ways.
# A. using index values.
# B. iterating directly over the strings.

# a = "SHERIYANS TEACHES INDUSTRY THINGS"# s=1 h=2 e=3 r=4 y=5 a=6 n=7 s=8
# #print(len(a)) # iska use islie krre hai taaki ye jo word hai inko ginte thodi baithenge.
# # for i in range(33): #length 1 se gini jaati hai aur range function 0 se
# #     print(a[i])
# for i in range(len(a)):
#     print(a[i])# kaise index value ka use krke ek string ko iterate krte h.

# 2nd tarika directly bhi kr sakte hai

# a = "SHERYIANS IS COOL"

# for i in a:
#     print(i)

# Break Continue and Else statement
#___________|__|____________ start se slash tak gaye fir ruke fir next slash se fir last tak chale.
# for i in range(1,21):
#     if i == 15:
#         break# jaha pe bhi break  aaya loop ruk jaega 14 par hi.
#     else:
#         print(i)

# for i in range(1,21):
#      if i == 15:
#          continue# jaha pe bhi continue aaya ye redirect krta hai value ko 15 print ni hoga.
#      else:
#         print(i)

# for i in range(1,21):
#     if i == 56:
#         print("break statement is executed")# break chala to else ni chalega.
#         break
#     print(i)

# else:
#     print("Break statement is not executed")# break agar nai chala to else chlega.

# Accept an integer and print hello world n times.
# n = int(input("please tell your number"))

# for i in range(n):
#     print("Hello World")

# Print natural number upto n.

# n = int(input("Please tell your number"))

# for i in range(1,n+1):
#     print(i)

# Reverese for loop print n to 1

# n = int(input("please tell your number"))

# for i in range(n,0,-1):
#     print(i)

#Take a number as input and print its table.

# n = int(input("please enter your number to give the table"))

# for i in range(n,(n*10)+1,n):
#     print(i)

# new method 
# n = int(input("which table you want : - "))

# for i in range(1,11):
#     print(f"{n} * {i} = {n*i}") # is method se bhi kara sakte hai print table

# sum upto n terms

# n = int(input("please tell your number:- "))

# sum = 0

# for i in range(1,n+1):
#     sum = sum + i


# print(f"your sum is {sum}")

# Factorial of a number

# n = int(input("please tell your number:- "))

# fact = 1

# for i in range(1,n+1):
#      fact = fact * i


# print(f"your factorial is {fact}")

# print the sum of all even & odd number in range separately

# n = int(input("please tell your number :- "))
# even = 0
# odd = 0
# for i in range(1,n+1):
#     if i%2 == 0:
#         even = even + i
# else:
#        odd = odd + i

# print(f"your even and odd sum are {even} , {odd}")

# factors 
 
 # if i talk about factors of 12 remainder 0 aana chaiye

# n = int(input("please tell your number :-"))

# for i in range(1,n+1):
#    if n%i == 0:# % mode hai iska mtlb remainder 0 ajae to print kro
#         print(i)

# accept a number and check if it a perfect number or not a number whose sum of factors is equal to the number itself

#Ex- 6= 1,2,3 = 6
# n = int(input("check your number is perfect or not :-"))
# sum = 0
# for i in range(1,n):
#     if n%i == 0:
#         sum = sum + i

# if sum == n:
#     print("your number is perfect")
# else:
#     print("not a perfect number")

# Check whether the number is prime or not
# wo number jinka sirf 2 hi dividend ho

# n = int(input("check your number is prime or not :-"))

# count = 0

# for i in range(1,n+1):
#     if n%i == 0:
#         count = count + 1

# if count == 2:
#     print("your number is prime")
# else:
#     print("your number is not prime")


# reverse string without usind build function

# a = "SAMMAS"

# b = ""
# for i in range(len(a)-1,-1,-1):
#    b = b + a[i]


# if b == a:
#    print("your string is pallindrome")

# else:
#    print("its not a pallindrome")

# count all letters,symbols and digits from a given string

# a = "sdfsogn12345@#$%^&*"

# char = 0
# dig = 0
# spchr = 0

# for i in a:
#    if i.isdigit():
#         dig +=1
#    elif i.isalpha():
#       char+=1
#    else:
#       spchr +=1

 # print(f"your digits are{dig}\nyour alphabets are {char}\nyour special characters are {spchr}")

# print(dir(str))

# While Loop

# you have previously taken the information of loops and you also know conditional statements it is going to be easy for you to understand this now.

# The while loop repeats a block of code as long as a condition is True. it is useful when the number of iterations is unknown before execution.

#while condition:
     # # Code to execute

# So there is not much that you have to understand about while loop it also have break, continue and else.

# Now you just have to find out which loop will be used on what questions.

# if i print 1 to 30
# a = 1 

# while a <= 30:
#     print(a)
#     a = a + 1

# while loop questions

# Separate each digit of a number and print it on the new line.

# a = int(input("tell your number"))

# while a > 0:
#     print(a % 10)
#     a = a //10

# accept a number and print it reverse.
 
# a = int(input("tell your number"))

# rev = 0

# while a > 0:
#     rev = rev *10 + a % 10
#     a = a //10 # 
# print(rev)

# accept a number and check if it is a pallindromic number (if number and its reverse are equal)

# a = int(input("please tell your number"))

# copy = a
# rev = 0

# while a > 0:
#     rev = rev *10 + a % 10
#     a = a //10

# if copy == rev:
#     print("pallindromic number")
# else:
#     print("not a pallindromic number")

# create a random guessing game by while loop


# i use simple library for guessing game

# import random

# num = random.randint(1,10)

# tries = 0

# while True:
#    guess = int(input("please guess your number between 1 and 10 :- "))


#    if num == guess:
#     tries +=1
#     print("you are right you guessed the number is {tries} tries")
#     break

#    elif num < guess:
#        print("number is high")
#        tries +=1

#    elif num > guess:
#        print("number is low")
#        tries +=1

#    else:
#     tries +=1
#     print("sorry you are wrong")

# import random

# num = random.randint(1,100)

# tries = 0

# while True:
#     guess = int(input("Please guess the number between 1 to 100 :- "))

#     if num == guess:
#         tries +=1
#         print(f"You Guess Right Number by the {tries} tries")
#         break
    
#     elif num < guess:
#         print("number is high")
#         tries +=1

#     elif num > guess:
#         print("number is low")
#         tries +=1

#     else:
#         tries +=1
#         print("sorry you are wrong")

# ---FUNCTION---

# FUNCTION in python group reusable code into a block that can be executed by calling the function name. this helps avoid repetition and makes programms modular and readable.

# there are many in-build function in python like print(),input(),len()etc.

# but you can create your own function and they are called as user defined functions. to make your own function you have to use def keyword and then name the function
# .After this you have to call the function using name() and parenthesis.

# function python me bahut saare create kar sakte ho jaise water ek function hai usko mai chaahe jitni baar call kr sakta hoo. sirf water ke naam se paani ke naam se nai.

# def greet():# khud ka function create def se hoga
#     print("Hello, Welcome to Python!")# aese create krte hai function

# greet() # Calling the function

#def Hello():
    #print("this is a hello function so i am doing hello")

# Hello()

# Parameters and Arguments are in Functions 

# First thing i want to talk about is parameters, parameters are variables listed inside the function definition.
# For making the function we have to accept inside the parenthesis of the function.

# def greet(name): #'name' is a parameter
#     print("Hello, {name}!")

# def sum(a,b):
#     print(f"The sum of your number is {a + b}")
# # the thing you accept is parameters
# # the thing you provide to parameters is argument.

# sum(12,12)
# sum(45,46)# iska use islie krre hai kyuki multiple time call kar sakte hai.
# sum(23,34)
# 
# def greet(name): # name is an parameter.
#     print(f"Hello, {name}!")

# greet("Alice") # "Alice" is an argument.

# There are 3 types of argument that we can pass to parameters,positional argumnet.default argument,keyword argument.For understanding these we will first see examples.
#Positional Arguments
# def add(a, b):
#     return a + b

# print(add(3,5)) # 3 is assigned to 'a', 5 to 'b'
# Positional arguments

# def hello(name,age):
#     print(f"your name is {name} and your age is {age}")

# hello(age = 22, name = "Akarsh")
# hello(age = 21, name = "Sameer")

# def sum(a,b=45):
#     print(f"the sum is {a+b}")

# sum(12)

# def sum(a,b=45):
#     print(f"the sum is {a+b}")

# sum(12,34)

# default argumnet 

# def introduce(name, age):
#     print(f"I am {name} and i am {age} years old.")

# introduce(age=25, name="John")

# Keyword Argument

# def greet(name="Guest"):
#     print(f"Hello, {name}!")

# greet() # using default value is guest
# greet("SAM") # using SAM

# -----CHECK THE STRING IS PALLINDROME OR NOT-----
# def pallindrome(st):
#     rev = ""
#     for i in range(len(st)-1,-1,-1):
#         rev = rev + st[i]

#     if rev == st:
#          print(f"{st} is a pallindrome")
#     else:
#         print(f"{st} is Not a pallindrome")

# pallindrome("NAMAN")
# pallindrome("SAMEER")

# def hello():
#     return("hello how are you")

# hello()# ye value ko retrurn krta hai islie. 
# print(hello())# Aese krte hai.

# ----DATA STRUCTURES IN PYTHON-----
# Data ko structured way me represent krne ko kahte hai
# in-build data structures 
# * data structures are used  to store,organize and manipulate data efficiently. Pyhton provides several built-in data structures.
# And for storing multiple values we will again use variables.
# Now in python we have 4 types of in-build data structures List,Tuple,Dictionary,Set.

# Custom Data strucutres.
# now there are some custom data structures as well like stack,queue,linked list,graph etc.
# and around these data structures there are some algorithms like searching alogorithm storing algorithms.
# and this is why the study is called data structures and algorithm.
# Lets be clear this python notes are not for the dsa this will cover all the in-build data structures.

# ----THE FIRST DATA STRUCTURE IS LIST Powers----

# Before starting we need to understand some of the terminology.
# * Mutable- Mutability refers to whether an object's value can  be changed after creation. And list allows this.
# *Duplicates- we know data structures are used to store multiple values so duplicates means same value occuring multiple time.list allows this
# *Ordered- list maintains ordered data structures maintains the sequence of elements as  they were inserted.This means you can acess elements using their position(index)
# *Heterogeneous- List have heterogeneous nature that means we can have multipledata types inside the list.
# 
# List basics 
# 
#  first we have to know what is the syntax of list and how to create a list we have to use square brackets{[]}.
# Syntax of list

# a = [12,13,14,15,16,34.5,True,print()]

# print(a[0:7])

# Define a list
# numbers = [10, 20, 30]

# Modify the value at index 1 (2nd elemet)
# numbers[1] = 99

#print the updated list
# print(numbers) # output is (10, 99, 30)

# list traverse

# a = [12,13,14,15,16,34,5]

# 1st way using index

# for i in range(len(a)):
  #  print(a[i])

# 2nd way directly on values

# for i in a:
 #   print(i) 

# Mothods of List

# print(dir(list))
# help(list)

# Numbers.append method
# l = [1,2,3,4,5]

# l.append(6) append kya krta hai last me jodta hai digit ko
# l.append(9)

# print(l)

# numbers.insert method

# insert beech me jodta hai digit ko
# l = [1,3,4,5]

# l.insert(1,2) # 1 likha islie haui counting 0 se start hoti hai 2 value haui jo daalni hai

# print(l)

# numbers.extnd method
# ekhatta 3,4 elements jakar jud jaaenge

#l = [1,2,3,4,5,6]

#l.extend([9,10,11,12]) # is tarike se jud jaate hai elements

# print(l)

#numbers.remove method 
# remove the first occurence agar mai koi value jaise repeat hui hai usko remove kru to first waali hogi baad wali nai 

# l = [1,2,3,4,5,6,7,8]

# l.remove(2)

# print(l)

# popped item method
# l = [1,2,3,4,5,6,7,8]

# popped_item = l.pop(3)

# print(l)

# indexmethod
# find the index 
# numbers = [1,2,3,4,5,6,7,8]

# index = numbers.index(4)

# print(index)

# count method

# numbers = [1,2,3,4,5,6,7,8,5,3,3] # so count the numbers method the number how many time repeated.

# count_3 = numbers.count(3)

# print(count_3)

# Sort the list in ascending order method\

# numbers = [1,2,3,4,7,6,5,8,10,15,12]

# numbers.sort() ascending order me jamana 

# print(numbers)

# Numbers reverse mewthod

# numbers = [1,2,3,4,5,6,7,8,5,3,3]

# numbers.reverse() # reverse the list order.

# print(numbers)

# Create a copy of list method

# numbers = [1,2,3,4,5,6,7,8,5,3,3]

# new_numbers = numbers.copy()

# print(new_numbers)

# Numbers.clear Method

# numbers = [1,2,3,4,5,6,7,8,5,3,3]

# numbers.clear() # Removes all element from the list

# print(numbers)

# print positive and negative elements of an list.

# l = [-45,67,12,-68,-69,34]

# print("positive elements are")
# for i in l:
#     if i >= 0:
#         print(i)

# print("negative elemnets are")

# for i in l:
#     if i < 0:
#         print(i)

# Mean of list element.

# l = [23,24,45,67,88,98,67]

# sum = 0

# for i in l:
#     sum = sum + i

# print(sum/len(l))

# Find the Greatest element and print it index too.

# l = [12,45,69,120,170,245,200]


# largest = l[0]

# for i in range(len(l)):
#     if l[i] >largest:
#         largest = l[i]
#         index = i

# print(f"your largest number is {largest} at index {index}")

# l = [ 34,23,45,122,300,1234,32,21]

# largest = l[0]
# index = 0

# for i in range(len(l)):
#     if l[i] > largest:
#         largest = l[i]
#         index = i

# print(f"your largest number is {largest} at the index {index}")

# Print a second largest number

# l = [12,11,34,25,45,54,33,97,103,500,120,321,432,]

# largest = l[0]
# sec_largest = l[0]
# index1 = 0
# index2 = 0

# for i in range(len(l)):
    
#     if l[i] > largest:
#         sec_largest = largest
#         index2 = index1

#         largest = l[i]
#         index1 = i
#     elif l[i] > sec_largest :
#       sec_largest = l[i]
#       index2 = i

# print(f"your second largest value is {sec_largest} at the index {index2} and your largest value is {largest} at the index {index1}")

# a = [12,13,14,15,16]

# for i in range(len(a)-1):
#     if a[i] < a[i+1]:
#         continue
#     else:
#         print("your list is not sorted")
#         break
# else:
#     print("your list is sorted") # ye islie chala kyuki andar jo else hai break nai hua islie print hua hai.

# a = [1,2,3,4,5,6,7,0]

# for i in range(len(a)-1):
#     if a[i] < a[i+1]:
#         continue
#     else:
#         print("your numbers is not shorted")
#         break
    
# else:
#     print("your numbers is sorted")

# ----Tuples Powers----

# Before starting we need to understand some of the terminology.
# . immutable- Tuples are not mutable you cannot change the values of tuple.
# . Duplicates- you can have duplicate values in tuples there are no restriction.
# . Ordered- Set are ordered and you can access them through index values.
# . Heterogenous- set also have heterogenous nature and can have different types of data structure in tuple.

# How to make a tuple
# a = (1,2,3,4,5)

# print(type(a))

# a(0) = 12

# print(a[2])
# print(a) # isme change nai hoti values
# heterogeneous tuples 
# a = (1,2,3,4,5,5,5.5,print(),"hello")
# list ki tara hai immutable nature hota hai change ni hoti.
# for i in range(len(a)):
#     print(a[i])
# index = a.index(5)
# print(index)
# count = a.count(5)

# print(count)
# a = (1,)

# print(type(a))

#--------SET POWERS----------

# if you want to create a set
# s = {}# agar aap aese likhoge to ye dictionaries.

# s = {1,2,3,4,5,5,6}

# print(s) # set ki power ye h duplicates value print ni hoti h

# a = 12
# b = hash("Hello")
# print(b)

# c = hash((1,2,344))

# print(c)

# a = {1,8,9,"hello",2,3,4,5}

# for i in a:
#     print(i)

# ------SET TRAVERSING-------
# A set cannot be traverse using the index value cause it is unordered and has no index.
# So many times it will give random values. you can which th video for complete understanding.

# 
# A = {1,2,3,4,5}
# B = {4,5,6,7,8}

# a.remove()
# a.pop()
# s = a.union(b)
# aese bhi apan print kara skate h.
# print(A | B) # Union
# print(A & B) # Intersection
# print(A - B) # Difference
# print(A ^ B) #Symmetric Difference

# print(A)

# d = {}# dictionaries ke andar value nai de sakte warna wo ek set hojati h.
# d = {1:"hello",2:56} # dictionaries me keys store ki jaati h
# d = {10:100,20:200,30:300,40:400}
# d[10] = 1000 # change krra hoo dictionaries me aese change hoti hai.
# d[50] = 500 #update krra hoo aese apan aur bhi value bhi add kr sakte hai.
# d[10] = 100 #creating
# del d[30] #deleting apan value ko change to kr sakte hai par key ko ni keyconstant hai jab koi nai key add krte hai tab hojaegi.

# print(d)

# ----Dictionaries Traversing-----
# dictionaries me loop kaise chalate hai

#d = {10:100,20:200,30:300,40:400}

#for i in d:#aese sidha value print kara skte hai
#    print(d[i])

# for i in d.values():
#     print(i)

# d.clear() #sab clear hojaega

# a = [1,2,3,4,5]

# b = a # value change hojati hai a ki

# b[0] = 100
# print(a)
# d2 = d.copy() # shallow copy method.

# d2 = d.get(10) #get dictionaries 

# print(d2)

# print(d.items())# items ke lie
#print(d.pop(10))#key se value ko print krnta h
#print(d.popitem()) #key value pair ko nikalta h 
# help(dict)

#---Practice question of dictionaries.
# write a python dictionaries to merge two python dictionaries.

# d1 = {10:100,20:200,30:300}
# d2 = {40:400,50:500,60:600}


# for i in d2: # yaaha par maine loop chalaya ki d2 se value d1 me merge hojae
#        d1[i] = d2[i]

# print(d1)

# ----SUM OF TWO DICTIONARIES----

# d1 = {10:100,20:200,30:300}
# sum = 0

# for i in d1:
#     sum = sum + d1[i]

# print(sum)

# Count a frequency of each element in a list?

# a = [1,1,1,2,2,2,3,3,3,4,4,4,5,5,6,7,8]

# d = {} #dictionaries banakar apan frequency print karaenge.
# for i in a:
#     if i in d.keys():
#         d[i] +=1
#     else:
#         d[i] = 1

# print(d)

# Write a python program to combine two dictionary by adding values to adding keys 

# d1 = {10:100,20:200,40:300}
# d2 = {40:400,50:500,60:600}

# for i in d2:
#     if i in d1.keys():
#         d1[i] += d2[i]
#     else:
#         d1[i] = d2[i]

# print(d1)

#----------EXCEPTION HANDLING---------------- 

# ---ERRORS---

# errors occur due to mistakes in the code that prevent it from running.These can be syntax errors or logical errors.

# Syntax errors 
# print("Hello World" #Missing closing parenthesis
# Now this above code will give the error of syntax.

# indentation Errors
# def func():
# print("hello") #no indentation
# you already know what is indentation and if you don't follow it you will get the error.

#-----EXCEPTION------

# Exception are unexpected events or errors that occurs during the execution of a program.which disrupts the normal flow of the program.

# a = int(input("tell your number :- "))

# print(10/a)# agar mai a = 0 likhta hoo to zero division error arha hai uski wajah se mera jo done the division wala print karana hai wo print ni hua hai.
# Isi ko exception handling kahte hai
# jaise mere paas 600-700 line kaa code hai is zero ki wajah se khuch print hi nai hoga.
# print("ok i have done the division")

# print("start")
# print(10 / 0) #Raises zero divisionerror
# print("End") # This time will never run

# yaha par jaise maine print karaya to start print to hogya par jaha 0 agya uski wajah se next ki line print ni hopai isi ko exception kahte hai
# ab ham seekh rahe hai ki is ko handle kaise krna hai by exception handling.
# now this is a zerodivisionerror and can be counted as exception and because of this exception the next line cannot be executed.

# exception handling ke lie khuch keywords.
# keyword  ----  purpose
# try      ----  wrap the block of code that might cause an exception.
# Except   ----  Handle the exception if it occurs
# else     ----  Run code only if no exception occurs
# finally  ----  Run code no matter what, whether there's an exception or not
# raise    ----  Manually throw an exception.

# a = int(input("tell your number :- "))

# try:# yaha par dekho try ke use se apan ne is error ko solve krlia
#     print(10/a)

# except Exception as err: # except ye likhna padega ab yaha par kisi bhi prakar error nai aaega.
#     print("sorry there is an err as {err}")

# else:
#     print("good there is no exception") # ye tab print hota hai jab execute hojata hai code.

# finally:
#     print("i will run no matter what") # ya to error aae ya na aae ye run hoga hi.

# print("ok i have done the division")

# age = int(input("tell your age :- "))

# try:

#     if age < 10 or age > 10: # yaha par apan khud error lagate hai condition se jaise niche kia h
#         raise ValueError("your age must be between 10 and 18")
#     else:
#         print("welcome to the club")

# except Exception as err:
#     print(f"an error occured as {err}")


# print("the club will start soon")

# ------FILE HANDLING-------

# What are files

# any name of extensions is known as file example-.py,.txt,.mp3 etc.

# File Handling

# file handling means creating reading updating,deleting(CRUD) operations that we can perform in files.
# Now lets see how to perform these operations that we can perform these operations in python.
# we have to use open() function to open a file in python.
# Now there are multiple modes to open the file 
# file ko handle krne ke lie hai.

# MODE |    DESCRIPTION
#  'r' | Read (default)-file must exist.
#  'w' | Write-creates file or overwrites.
#  'a' | Append-adds to end of file.
#  'x' | Create-creates a new file.fails if it exists.

# r = open("Sameer.txt",'w') create krta hai file ko 
# r = open("Sameer.txt",'a')# a append krta h yaani add krta hai 

# r.write("and now i am appending some content inside the file. ")

# r.close()

# with open("main.py", "r") as f: # read kr sakte ho r se.
#     content = f.read()
#     print(content)

# What is OOPS ?

# And our next approach is object oriented programming approach.

# class Addition:
#       def __init__(self, a, b):
#           print(a + b)

# obj = Addition(12, 12)

# OOPS (Object-oriented programming system) is a programming paradigm based on the concept of "objects",
#   which can contain data (attributes) and code (methods).

# I know it is tough to understand right now but it will be easy after learning there are many concepts that we have to learn like classes,objects,encapsulation,inheritance,polymorphism, etc. So lets start.

# apan ne padha imperitive approach

# a = 12
# b = 12
# print(a + b)

# uske baad 2nd approach padhi functional approach

# def addition(a, b):
#     return a + b

# print(addition(12, 12))# isme ek baar assign krdo baar baar code ni likhna padta.
# print(addition(45, 45))

# ab oops approach padhenge.
# ye bank management me kaam aata hai.

# -----CLASS-----

# A class is like a blueprint or template for creating objects.
# Thinks of a class like the blueprint of a house. it defines what the house should have (rooms, windows, etc.) but doesn't build the house. An object is the actual house built using that blueprint.

# syntax
# class Car:
#     brand = "Toyota" 

# A class is also created with a basic keyword class and a name in front of it.
# Creating a class is super simple now lets see what is inside class.There are 2 types of things inside class attributes and methods.
 # Attributes-variables defined inside the class are Attribute.
 # Methods- Functions defined inside a class are Methods.

# class Factory:
#     a = 12 # attribute class ke andar bana hai

#     def hello(self): #method
#         print("how are you")

#     print("hello how are you i am getting initialized")
        
# print(Factory().a)

# Factory().hello()

# New class create

# class Animal:
#     type = "Cat" # attribute class ke andar bana hai

#     def sound(self): #method
#         print("Meow")

# Directly accessing attribute and method using the class
# print(Animal().type) # Access attribute

# Animal().sound()  # call method

# ----OBJECTS----

#       -------------
#       |Bag Factory|
#       -------------
#             |
#             |
#       -------------
#       |Requirement |
#       -------------
#       |     |      |
#       |     |      |
# (material) (Zips) (Pockets)

# for understanding the objects first look at this example you have a bag factory
# and that factory requires material of the bag. number of zips you need in that bag and number of pockets you need in your bag.
# So this is kind of a blueprint and using this blueprint reebok, campus and some other companies provided their requirement and created their bags.
# thus these companies became objects who created their bags using the blueprint.

# class Factory:
#      a = 12 # attribute class ke andar bana hai

#      def hello(self): #method
#          print("how are you")

# obj = Factory() # ye jo class thi iska acess object ko milgaya.

# obj2 = Factory()

# obj3 = Factory()

# ----CONSTRUCTOR----

# Constructor hota hai parameters magne ke lie.

# you saw last example where we wanted material. zips and pockets from the user to create an object.

# If we talk about a function we can ask the user using parameters but in class we can't have parameters for that we use constructor.

# A constructor is a method that runs automatically when we call a class and this constructor function will target the objects location

# class Student:
#    def __init__(self, name):
#       self.name = name #instance attribute

# # Creating an object with a value
# s = Student("Sameer")

# Accepting the attribute
# print(s.name)
# Constructor ke through aap samne wale se cheeze mang sakte ho.
# class Factory:
#    def __init__(self,material,zips,pockets):
#       self.material = material
#       self.zips = zips
#       self.pockets = pockets

#    def show(self):
#        print(f"your object detail are {self.material}, {self.pockets},{self.zips} ")

# reebok = Factory("leather",3,2) #object create kia

# campus = Factory("nylon",3,3) # object hai 

# print(campus.pockets) # is tarike se print krdenge.

# reebok.show()

# -----ATTRIBUTES AND METHODS-----

# * Class attribute- A normal variable created inside a class is a class attribute and thats it.
# Attributes are just variables define  inside a class and those are attribute

# *Instance attribute- A attribute created using an instance like self.name,self.age etc. it is known as instance attribute.
# Apke object ki koi location usko instance bolte hai self ke sath 

# class Animal:
#     name ="Lion" #classs attribute

#     def __init__(self):
#         self.age = age # instances attribute 

# Types of Methods

# *Instances Method-An instance method works with instance(object) of the class. This method can acess and modify instance attribute.

# class MyClass:
#     def instance_method(self):
#         print("This is an instance method") # isi ko instance method kahte hai.

# class Animal:
#    name ="Lion" #classs attribute

#    def __init__(self,age):
#       self.age = age #instance attribute

#    def show(self): # instance method
#       print("how are you")

# Class Method-

# This method works with the class itself it will not target the instance (object). we have to use @classmethod decorator for creating the class method and it takes cls as their first parameter.
# class MyClass:
#     @classmethod
#     def class_method(cls):
#         print("This is a class method")

# class Animal:
#      name ="Lion" #classs attribute

#      def __init__(self,age):
#         self.age = age 

#      def show(self): # instance method
#        print("how are you your age is {self.age}")

#      @classmethod
#      def hello(cls):
#          print("how are you brother")

#------Static Method------

# This method doesn't access class or instance directly it also uses a decorator @staticmethod it just acts like a regular function placed inside a class.

# class MyClass:
#     @staticmethod # static method
#     def static_method():
#         print("This is a static method")

# @staticmethod
# def static():
#     print("how are you")

# obj = Animal(12)

# obj.hello()

#----There are four pillars of oop

# 1--INHERITANCE---

# in general terms inheritance means properly or any possesion that comes to an heir.
# in python inheritance  work between classes inheritance allows a child class to inherit properties and behavior from another class parent class and child class inherit parent class.
# benefits of using inheritance is:
# Code Reusability
# organized structure
# Easy to maintain and extend.

# Syntax of inheritance

# class Factorymumbai: # parent class / superclass
#     a = 12
#     def hello(self):
#         print("hello i am a method mentioned inside Factory")

# class Factorypune(Factorymumbai): # Child class/subclass
#     pass

# obj = Factorymumbai()

# obj2 = Factorypune()

# print(obj.a)

# print(obj2.hello())

# Now the inherited class has all the powers of parent class that means all the methods.attributes can accessed by the instance of child class as well.
# class Parent:
#    def speak(self):
#        print("I can speak!")

# class Child(Parent):
#     pass

#---Constructor in inheritance---

# ---Example---

# class Animal:
#     def __init__(self,name):
#         self.name = name

#     def show(self):
#      print(f"hello your name is {self.name}")

# class Human(Animal):
#     pass


# animal1 = Animal("LION") # this is an instances of main class
# person1 = Human("sameer") # this is an instances of child class.

# person1.show()
# animal1.show()

class Parent:
    def __init__(self, name):
        self.name = name

class Child(Parent):
    def display(self):
        print(f"my name is {self.name}")

child1 = Child("ayan")

child1.display()


    
