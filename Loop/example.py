# count = 0 
# while count<100:
#     print("programming is fun")
#     count=count+1
import random 
num1= random.randint(0,9)
num2= random.randint(0,9)
if num1 < num2 : 
    num1 , num2=num2 , num1 
    #expressions from a string-based or compiled-code-based input
answer = eval(input("What is " + str(num1) + " - " + str(num2) + "? "))
while num1 - num2 != answer:
 answer = eval(input("Wrong answer. Try again. \nWhat is " + str() + " - " + str(num2) + "? "))
print("You got it!")
  