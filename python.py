num = int(input())
print("Original type : ",type(num))
num_flo = float(num)
print("After float Conversion : ",type(num_flo))
num_flo *= 3.5
res = int(num_flo)
print("Final type : ",type(res))
print("Final value : ",res)

# PRECISION LOSS CHALLENGE
num=input()
float_num = float(num)
str_ver = float(str(num))
diff = float_num-str_ver
print(f"Float version: {float_num:.20f}")
print(f"String→float version: {str_ver:.20f}")
print(f"Difference: {diff:.20f}")

# Dynamic Data Switch
num = input()
print(type(num))
if not num.find(".")==-1:
    num=float(num)
    print(type(num))
else:
    num=int(num)
    print(type(num))

# STRUCTURED INPUT PARSER
sen = input()
words = sen.split(" ")
print(f"Name: {words[0]}")
print(f"Age next year: {int(words[1])+1}")
print(f"Height in cm: {float(words[2])*30.48:.2f}cm")

# Input Validation
num = input("Enter a number : ")
if not num.isdigit():
    print("Invalid Input")
else:
    num = int(num)
    print(f"Square : {num*num}, Cube : {pow(num,3)}")

# Operator Priority Puzzle
result = 5 + 2 * 3 ** 2 // 3 - 4
print(result)

# Bitwise Operator Logic
map method
a,b = map(int, input("Enter two integers : ").split())
print(f"AND: {a&b:03b}")
print(f"OR: {a|b:03b}")
print(f"XOR: {a^b:03b}")
print(f"Left shift: {a<< 1:03b}")
print(f"Right shift: {a>>1:03b}")

# If–Else Conditions
marks = int(input())
if(marks>=90 and marks<=100):
    print("Excellent")

elif(marks>=75 and marks<89):
    print("Very Good")

elif(marks>=50 and marks<=74):
    print("Pass")

elif(marks<50):
    print("Fail")
else:
    print("Error")

# LEAP YEAR VALIDATOR
year = int(input("Enter year : "))
if (year%4==0 and year%100 !=0) or (year % 400 == 0):
    print("Leap Year")
else:
    print("Not a leap year")

# REVERSE NUMBER & DIGIT SUM
num = int(input("Enter a num : "))
og = num
sum=0
rev=0
while num>0:
    dig = num%10
    sum+=dig
    rev=rev*10+dig
    num//=10
diff = og-rev
print("Reverse: ",rev)
print("Sum: ",sum)
print("Difference: ",diff)

# COMPOUND INTREST CALCULATOR

while True:
    prin = float(input("Enter Principal Amount : "))
    if(prin<=0):
        print("Not a Valid Amount")
    else:
        break
while True:
    rate = float(input("Enter Rate of Intrest : "))
    if(prin<=0):
        print("Not a Valid Intrest")
    else:
        break

while True:
    time = float(input("Enter Tenure : "))
    if(prin<=0):
        print("Not a Valid Tenure")
#     else:
#         break
# total = prin*pow((1+rate/100),time)
# print(f"Balance after {time} years : ${total:.2f}")
