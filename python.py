# num = int(input())
# print("Original type : ",type(num))
# num_flo = float(num)
# print("After float Conversion : ",type(num_flo))
# num_flo *= 3.5
# res = int(num_flo)
# print("Final type : ",type(res))
# print("Final value : ",res)

# PRECISION LOSS CHALLENGE
# num=input()
# float_num = float(num)
# str_ver = float(str(num))
# diff = float_num-str_ver
# print(f"Float version: {float_num:.20f}")
# print(f"String→float version: {str_ver:.20f}")
# print(f"Difference: {diff:.20f}")

# Dynamic Data Switch
# num = input()
# print(type(num))
# if not num.find(".")==-1:
#     num=float(num)
#     print(type(num))
# else:
#     num=int(num)
#     print(type(num))

# STRUCTURED INPUT PARSER
# sen = input()
# words = sen.split(" ")
# print(f"Name: {words[0]}")
# print(f"Age next year: {int(words[1])+1}")
# print(f"Height in cm: {float(words[2])*30.48:.2f}cm")

# Input Validation
# num = input("Enter a number : ")
# if not num.isdigit():
#     print("Invalid Input")
# else:
#     num = int(num)
#     print(f"Square : {num*num}, Cube : {pow(num,3)}")

# Operator Priority Puzzle
# result = 5 + 2 * 3 ** 2 // 3 - 4
# print(result)

# Bitwise Operator Logic
# map method
# a,b = map(int, input("Enter two integers : ").split())
# print(f"AND: {a&b:03b}")
# print(f"OR: {a|b:03b}")
# print(f"XOR: {a^b:03b}")
# print(f"Left shift: {a<< 1:03b}")
# print(f"Right shift: {a>>1:03b}")

# If–Else Conditions
# marks = int(input())
# if(marks>=90 and marks<=100):
#     print("Excellent")

# elif(marks>=75 and marks<89):
#     print("Very Good")

# elif(marks>=50 and marks<=74):
#     print("Pass")

# elif(marks<50):
#     print("Fail")
# else:
#     print("Error")

# LEAP YEAR VALIDATOR
# year = int(input("Enter year : "))
# if (year%4==0 and year%100 !=0) or (year % 400 == 0):
#     print("Leap Year")
# else:
#     print("Not a leap year")

# REVERSE NUMBER & DIGIT SUM
# num = int(input("Enter a num : "))
# og = num
# sum=0
# rev=0
# while num>0:
#     dig = num%10
#     sum+=dig
#     rev=rev*10+dig
#     num//=10
# diff = og-rev
# print("Reverse: ",rev)
# print("Sum: ",sum)
# print("Difference: ",diff)

# COMPOUND INTREST CALCULATOR

# while True:
#     prin = float(input("Enter Principal Amount : "))
#     if(prin<=0):
#         print("Not a Valid Amount")
#     else:
#         break
# while True:
#     rate = float(input("Enter Rate of Intrest : "))
#     if(prin<=0):
#         print("Not a Valid Intrest")
#     else:
#         break

# while True:
#     time = float(input("Enter Tenure : "))
#     if(prin<=0):
#         print("Not a Valid Tenure")
#     else:
#         break
# total = prin*pow((1+rate/100),time)
# print(f"Balance after {time} years : ${total:.2f}")
# Smart Calculator
# a,b,op = input("Enter 2 numbers and an operator :").split()
# a = int(a)
# b = int(b)
# if op=='+':
#     print("Sum is :",a+b)
# elif op=='-':
#     print("Diff is :",a-b)
# elif op=='*':
#     print("Mul is :",a*b)
# elif op=='/':
#     if b==0 and op=='/':
#         print("Cannot divide by zero")  
#     else:    
#         print("Div is :",a/b)
# elif op=='%':
#     print("Modulo is :",a%b)
# elif op=='//':
#     print("Div is :",a//b)
# else:
#     print(f"{op} is Invalid Operator ")

# Temperature Converter
# temp = float(input("Enter Temp : "))
# unit = input("Enter Unit(C/F) : ").upper()
# if unit=='C':
#     temp = (9*temp)/5+32
#     print(f"The temp in Fahrenheit is {temp:.3f}F")
#     if(temp>100):
#         print("Too Hot")
#     elif(temp<32):
#         print("Freezing")
#     else:
#         print("Normal")
    
# elif unit=='F':
#     temp = (temp-32)*5/9
#     print(f"The temp in Celsius is {temp:.3f}C")
#     if(temp>37):
#         print("Too Hot")
#     elif(temp<0):
#         print("Freezing")
#     else:
#         print("Normal")
# else:
#     print("The {unit} is NOT valid")


# STRINGS & LOOPS

# sen = input("Enter a String : ")
# words = sen.split(" ")
# vc = 0
# cc = 0
# digc = 0

# for word in words:
#     for i in range(len(word)):
#         if word[i] in "aeiouAEIOU":
#             vc += 1
#         elif word[i].isdigit():
#             digc += 1
#         else:
#             cc += 1
# print("Vowels :",vc)
# print("Consonents:",cc)
# print("Digits:",digc) 
# print("Spaces",len(words)-1)   

# S = input("Enter a String : ")
# res = ""
# for i in range(len(S)):
#     res = S[i]+res
# print(res)

# S = input("Enter a string :")
# unique = ""
# for ch in S:
#     if ch not in unique:
#         unique+=ch
# print(unique)

# Sen = input("Enter a Sentence : ")
# words = Sen.split()
# longest = max(words,key=len)
# print(longest,end="")
# print("(",len(longest),")")

# Password Validator

# while True:
#     password = input("Enter Password : ")
#     if len(password)<8:
#         print("Password should be atleast * characters")
#     else:
#         break

# Palindrome

# num = int(input("Enter a number : "))
# og = num
# rev=0
# while num>0:
#     dig = num%10
#     rev = rev*10+dig
#     num//=10
# if rev==og:
#     print("Palindrome")
# else:
#     print("Not a Palindrome")

# PATTERN
# n = int(input("Enter number of rows : "))
# for i in range(1,n+1):
#     for j in range(i):
#         print("*",end="")
#     print()

# n = int(input("Enter number of rows : "))
# for i in range(n,0,-1):
#     for j in range(i):
#         print("*",end="")
#     print()

# n = int(input("Enter number of rows : "))
# for i in range(n):
#     for j in range(n-i-1):
#         print(" ",end="")
#     for j in range(2*i+1):
#         print("*",end="")
#     print()

# DIAMOND PATTERN
# n = int(input("Enter number of rows : "))
# for i in range(n):
#     for j in range(n-i-1):
#         print(" ",end="")
#     for j in range(2*i+1):
#         print("*",end="")
#     print()
# for i in range(n-2,-1,-1):
#     for j in range(n-i-1):
#         print(" ",end="")
#     for j in range(2*i+1):
#         print("*",end="")
#     print()

# HALLOW PYRAMID
# n = int(input("Enter number of rows : "))
# for i in range(n):
#     for j in range(n-i-1):
#         print(" ",end="")
#     for j in range(2*i+1):
#         if j==0 or j==2*i or i==n-1:
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()

# PASCALS TRIANGLE
# n = int(input("Enter a number : "))
# for i in range(n):
#     num=1
#     for j in range(n-i-1):
#         print(" ",end="")
#     for j in range(i+1):
#         print(num,end=" ")
#         num = num * (i-j)//(j+1)
#     print()

# BUTTERFLY PATTERN
# n = int(input("Enter n :"))
# for i in range(1,n+1):
#     print("*"*i+" "*(2*(n-i))+"*"*i)
# for i in range(n-1,0,-1):
#     print("*"*i+" "*(2*(n-i))+"*"*i)

# Number palindrome pyramid
# n = int(input("Enter n : "))
# for i in range(1,n+1):
#     for j in range(n-i):
#         print(" ",end="")
#     for j in range(1,i+1):
#         print(j,end=" ")
#     for j in range(i-1,0,-1):
#         print(j,end=" ")
#     print()

# import streamlit as st
# st.title("Basic Calculator")
# num1=st.number_input("Enter first number",value=0,step=1)
# num2=st.number_input("Enter second number",value=0,step=1)
# operation=st.selectbox("Select Operation",
#                        ("Addition","Subtraction","Multiplication","Division"))
# result=0
# if st.button("Calculate"):
#     if operation == "Addition":
#         result=num1+num2
#     elif operation=="Subtraction":
#         result=num1-num2
#     elif operation=="Multiplication":
#         result=num1*num2
#     elif operation=="Division":
#         result=num1/num2
#     st.success(f"Result: {result:.2f}")

# correct_pin = "777333"
# attempts = 0
# while attempts < 3:
#     pin = input("Enter PIN: ")
#     if pin == correct_pin:
#         print("Access granted! Welcome.")
#         break 
#     else:
#         attempts += 1
#         remaining = 3 - attempts
#         if remaining > 0:
#             print(f"Wrong PIN. {remaining} attempts left.")
#         else:
#             print("Account blocked after 3 wrong attempts!")

# ----------------NUMBER GUESSING GAME---------------------------------------
# import random

# print("="*40)
# print("NUMBER GUESSING GAME")
# print("="*40)

# level = input("Enter Difficulty level (easy/hard): ").lower()

# if level == "easy":
#     low, high, attempts = 1, 50, 7
# elif level == "hard":
#     low, high, attempts = 1, 100, 5
# else:
#     print("Choose valid level!")
#     exit()

# secret = random.randint(low, high)

# print(f"\nGuess a number between {low} and {high}")
# print(f"You have {attempts} chances. Good luck!")

# chances = 0
# won = False

# while chances < attempts:

#     try:
#         guess = int(input(f"Attempt {chances+1}/{attempts}: "))
#     except ValueError:
#         print("Numbers only!")
#         continue

#     if guess < low or guess > high:
#         print("Guess within the range!")
#         continue

#     chances += 1
#     remaining = attempts - chances

#     if guess == secret:
#         won = True
#         break

#     diff = abs(secret - guess)

#     if guess < secret:
#         if diff <= 5:
#             print(f"🔥 Very close! Go higher ({remaining} left)")
#         else:
#             print(f"↑ Too low! Go higher ({remaining} left)")
#     else:
#         if diff <= 5:
#             print(f"🔥 Very close! Go lower ({remaining} left)")
#         else:
#             print(f"↓ Too high! Go lower ({remaining} left)")

# print("-"*40)

# if won:
#     print(f"Excellent! You guessed {secret} in {chances} tries!")

#     if chances <= 3:
#         print("Incredible — under 3 tries!")
#     elif chances <= 5:
#         print("Well done!")
#     else:
#         print("Made it just in time!")

# else:
#     print(f"Out of tries! The number was {secret}.")

# print("="*40)

# Collections

# lst = [x**2 for x in range(1,21)]
# print(lst)
# lst.reverse()
# print(lst)
# print(lst[::-1])
# print(max(lst))
# print(min(lst))
# print(lst.count(7))

# t = tuple(lst)
# print(t)
# print(t[-1])
# for i in t:
#     print(t.count(i),end=" ")
# print(t.index(64))

# l = [1,4,3,7,8,3,7,2,1,1,9,9,5,4,4]
# s = set(l)
# print(s)
# s.add(6)
# print(s)
# s.remove(10)#returns error
# print(s)
# s.discard(10)
# print(s)
# p=s.pop()
# print(p)
# print(s)

# s1={4,6,7,9,1,2}
# s2={1,2,8,9,0,4}
# print(s1|s2)
# print(s1&s2)
# print(s1-s2)
# print(s1^s2)
# print(5 in s1)

# d = {x:x*x for x in range(1,11)}
# print(d.get(4))
# print(list(d.keys()))
# print(d.values())
# d[3]=24
# print(d[3])
# k=d.pop(2)
# print(k)
# for k,v in d.items():
#     print(f"{k} : {v}")

# even = [x for x in range(1,51) if x%2==0]
# print(even)
# str = "Aeiou rstuiae"
# s = {ch for ch in str if ch.lower() in "aeiou"}
# print(s)
# d = {x:x**3 for x in range(1,11)}
# print(d)
# s = tuple(x**2 for x in range(1,11))
# print(type(s))

# l = list(map(int,input().split(" ")))
# pos = [x for x in l if x>0]
# print(pos)
# l.sort(reverse=True)
# print(l[1])
# m = [5,4,3,2,1]
# l.extend(m)
# print(list(set(l)))
# nested_lst = [[1,2,3],[4,5,6],[7,8,9]]
# flatten = [x for row in nested_lst for x in row]
# print(flatten)

# lst = [10,20,30,40,50]
# res = tuple((i,val) for i,val in enumerate(lst))
# print(res)
# l = [(i,j) for i in lst for j in lst if i<j]
# print(l)
# k=3
# rotated = lst[k:]+lst[:k]
# print(rotated)


# QUIZ GAME
questions = ("1.What is the powerhouse of the cell?",
             "2.How many bones does human body consist of?",
             "3.What is the largest Continent?",                                                                                                                   
             "4.1km = How many meters?")
options = (("A.Nucleas","B.Mitochondria","C.Plasma","D.Blood"),
           ("A.202","B.304","C.206","D.108"),
           ("A.Asia","B.Africa","C.South America","D.Antartica"),
           ("A.100","B.1200","C.10","D.1000"))
ans = ('B','C','A','D')
question_num=0
score=0
guesses=[]
for q in questions:
    print('_'*20)
    print(q)
    print('-'*20)
    for o in options[question_num]:
        print(o)
    guess = input("Enter Option(A,B,C,D):").upper()
    guesses.append(guess)
    
    if guess==ans[question_num]:
        score+=1
        print("CORRECT")
    else:
        print("INCORRECT")
        print(f"{ans[question_num]} is the correct answer")
    question_num+=1

print("***********RESULTS***********")
print("answers:",end="")
for a in ans:
    print(a,end=" ")
print("\nguesses:",end="")
for guess in guesses:
    print(guess,end=" ")

print(f"\nYou guessed {score} correct")
print(f"SCORE : {((score)/len(questions))*100}")
