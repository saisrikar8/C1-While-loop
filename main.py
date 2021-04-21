
'''

02/11/2021

Review:

Boolean Operator

- Used when more than one condition are being used


and
or
"not" operator is used to find the opposite of a boolean

Random Number Generator:

import random(importing random library)

variable = random.randint(start, end)
===========================================================

While loop:

Repeats a set of statements as long as a condition is True.

Formula:

while(Condition):
  BODY

else:
  BODY

Rule:
A loop bcomes infinite loop if a condition never becomes FALSE. An infinite loop might be useful in cclient/server programming where the server needs to run continuously.

However, you must cuse cation when using loops because of the possibility that this condition never resolves a FALSE value. To avoid an infinite loop, make suree to use a variable and keep track of its value. You can increment and decrement it.

Ex1)

integer = 1

while(integer < 10):
  print("This statement prints forever")
  integer += 1 # incrementation
else:
  print("This is the end of the while loop")

Ex2)

counter = 0

while counter < 3:
  print("Inside Loop")
  counter += 1

else:
  print("Inside else")
'''

'''
Exercise 1:
Expected outputs:
hello
Python
Python
Evergreen
Evergreen
Evergreen
2021

student = 0

while(student <= 6):
    if(student < 1):
      print("hello")
    elif (student < 3):
      print("Python")
    elif(student < 0):
      print("bye")
    elif(student <= 5):
      print("Evergreen")
    else:
      print("2021")
    student += 1
'''

'''
Exercise 2:
Expected outputs:
  hello
  Python
  Python
  bye
  Evergreen
  Evergreen
  2021

student = 5

while(student <= 11):
  if(student < 6):
    print("hello")
  elif(student <= 7):
    print("Python")
  elif(student <= 8):
    print("bye")
  elif(student < 11):
    print("Evergreen")
  else:
    print("2021")

  student += 1
'''
