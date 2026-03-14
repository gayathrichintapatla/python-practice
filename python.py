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

<<<<<<< HEAD
=======
# # while True:
# #     time = float(input("Enter Tenure : "))
# #     if(prin<=0):
# #         print("Not a Valid Tenure")
# #     else:
# #         break
# # total = prin*pow((1+rate/100),time)
# # print(f"Balance after {time} years : ${total:.2f}")


# # Smart Calculator
# # a,b,op = input("Enter 2 numbers and an operator :").split()
# # a = int(a)
# # b = int(b)
# # if op=='+':
# #     print("Sum is :",a+b)
# # elif op=='-':
# #     print("Diff is :",a-b)
# # elif op=='*':
# #     print("Mul is :",a*b)
# # elif op=='/':
# #     if b==0 and op=='/':
# #         print("Cannot divide by zero")  
# #     else:    
# #         print("Div is :",a/b)
# # elif op=='%':
# #     print("Modulo is :",a%b)
# # elif op=='//':
# #     print("Div is :",a//b)
# # else:
# #     print(f"{op} is Invalid Operator ")

# # Temperature Converter
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
>>>>>>> 270831531f211316a9bad65b55e6d85fe41090c5
# while True:
#     time = float(input("Enter Tenure : "))
#     if(prin<=0):
#         print("Not a Valid Tenure")
#     else:
#         break
# total = prin*pow((1+rate/100),time)
# print(f"Balance after {time} years : ${total:.2f}")
<<<<<<< HEAD
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
n = int(input("Enter n : "))
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end="")
    for j in range(1,i+1):
        print(j,end=" ")
    for j in range(i-1,0,-1):
        print(j,end=" ")
    print()
=======

>>>>>>> 270831531f211316a9bad65b55e6d85fe41090c5
