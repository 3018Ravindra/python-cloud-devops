# Goal - "Learn how to talk to computer"

Topics 

Variables (memory boxes)

Data types (int, float, string)

Input / Output

Loops (repeat work)

function (reuse work)

# Why This Matters in DevOps
 
 * Because automation scripts are:

 Input → Decision → Repeat → Output
 Monitoring
 Scaling
 Deployment
 Health check

ALL use these.

# Day 1 - Things i have learned.

- understand variable concept
- understand printing/output concept
- understand input concept

# Why does the variable concept exists?
- When computer runs a program, it needs a place to temporarily store information.
- computer cannot remember things like humans, so it uses RAM but RAM is hug
- so we created variable i.e = "Named Memory Location"

# Why does the output concept exists?
- why do we output?
- ouput is created to see machine thinking
- In a layman term it is saying "computer just show me what you have stored"
- print()

# why does the input concept exists?
- why do we need input?
- Because real world is dynamic.
- CPU today = 20
- CPU tomorrow = 90

- So script must accept outside data. 
Input means: 
- Bringing real world data into program.
- ravi = input()

# Day 2 - Data Types in Python
# Goal - To make the computer behave correctly with the data you give it.

- Imagine computer memory is like huge warehouse.
- Inside warehouse you can store-
- numbers
- words
- yes/no
- collections

-- The simple question computer asked! What kind of data i am storing?

 -- It cannot “guess” what you mean.
- If you give:-
-number → it will do math
-text → it will join
-boolean → it will decide
-So data type tells computer:
# “How should you treat this data?”

 STARTING DATA TYPES

 Why Data Types exist

 What is Data Type

 Types used in DevOps scripts

 How computer behaves differently with each


# Type 1 → INTEGER (int)
- Sometimes we need to store countable quantities.

- which is likely to be whole numbers

So computer needs a type that:

-stores exact count

-supports math

-uses less memory

-So Integer exists.
 
 - example 
  Ravi = 25

  - a = 10
  - b = 20
 -  print(a + b)
- it shows computer stores number.

 - Computer adds.

-Because integers support arithmetic.  

# Data type -FLOAT
- Sometime value is measured
- e.g
- temperature
- response time
- memory usage
------------ These are fractional.
--Then computer needs:
- decimal storage type
- So, FLOAT Exists.
----e.g-

Ravi = 179.5

# an example of FLOAT data type

x = 1.5

y = 2.5

print(x + y)

# Data Type - String
- why does it exists?

- Computer works with many things.

Some things are:

✅ Numbers → like CPU = 90
✅ Decisions → like service_running = True
✅ Names / Messages → THIS is where STRING is needed

- What is String?

- STRING = TEXT

- anything we can read like humans is STRING

# How We Write STRING in Python 

-  We use quotes ""

- Ravi = "34"

- now computer understand that this is TEXT

- Do not do math on this

# What Computer Does With STRING

- Computer can: Join text

- a = "hello"
- b = "world"
- print(a + b)
- output ---
- helloworld


# Data type - BOOLEAN

- Why Boolean does exists?

- computer must take decisions:

- usually, it is depend upon YES/NO

- Boolean = True/False

Only two values exist.

True

False

# How We Write BOOLEAN in Python

- No quotes.

- First letter capital.

- service_running = True

- Computer understands:

👉 This is decision value.

- Boolean is mainly used in conditions.

# Learning Condition! 
- Why does condition even exists?
- if computer always does same thing- will lead to do disaster
- So computer must first observe situation, then decide.
- This observation + Decision = CONDITION
> a human example 
> if raining - take umbrella
> if sunny - take cap
- Here we did not act randomly, We checked condtions

-- if situation is true --> take action
# Else --> do nothing.
- it is nothing but-- comparing current state vs expected state.

- Expected safe CPU = 60

- Current CPU = 80

--> Mismatch- take action.

# ELIF condition (Multiple decision)

- Real world rarely has only two states:

- examples are -

- very high

- medium 

- normal

-- so program must choose best action among many.

- Thus - ELIF condition exists.

# What is Nested Condition?

- condition inside another condition

- meaning -- program checks one thing, then inside that checks another thing.

# Why nested condition exists?

- sometimes one decision is not enough-

- main situation

- then deeper situation

--> because real world is layered

# Starting loop (What is Loop)

- Loop = Doing same things again and again until condition met.

# Types of loops in python 

- While loop 

-- structure of while loop 

while condition: 
      action 

-- Meaning = as long as condition is true --> keep running      

# Why loop are important in DevOps

- Scan many logs 

- deploy many instances 

- retry commands

- monitor continuously

-- loop make script (work like machine)

## loop helps program do repetitive work without rewriting code.


# Infinite loop

- it exists to monitor continuously, listen for events. run servers

- so loop must run forever.

# Break (stopping loop manually)

- loop condition may not always be predictable. So we need emergency exit.

- That exit is - BREAK, BREAK = STOP

# How Program Thinks

- loop starts

- prints 1

- prints 2

- prints 3

-- sees break >> exits loop immediately.

# Continue (Skip one round)

- sometimes we don't want to stop loop, we just want to skip one cycle. So programming invented:

- "Continue"

# Summary - 

- Infinite loop - runs forever

- break - Stop Loop completely

- Continue - Skip one turn

