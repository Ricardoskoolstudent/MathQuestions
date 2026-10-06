# This is where your code goes!
import random

numQuestions = int(input("How many questions do you want?"))
lowest_num = int(input("What's the lowest number?"))
highest_num = int(input("What's the highest number?"))
print ("What operation would you like to do?")
print ("1 - Add")
print ("2 - subtract")
print ("3 - Multiply")
print ("4 - divide")
operation = int(input())
score =0
for i in range(1,numQuestions+1):
    num1 = random.randint(lowest_num,highest_num)
    num2 = random.randint(lowest_num,highest_num)
    num1 = num1 + num2
    answer = num1// num2

    print(f"{num1} / {num2} = ?")
    userAnswer = int(input())
    if userAnswer == answer:
        print("Correct")
    else:
        print("Incorrect", answer)