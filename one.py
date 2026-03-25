from xml.dom.minidom import Notation


print("Ravi is leaning python for devops and cloud")

# program about variable

Ravi = 25
print(Ravi)

Ravi = input()
Ravi = int(input())

cpu = 40
cpu = 50
cpu = 80
print(cpu)


service = "python"
status = "running"
print("service", service, "is", status)

# data type integer
a = 10
b = 45
print(a+b)

# data type float
a = 12.7
b = 78.3
print(a+b)

# data type string
Ravi = "25"
a = "Ravi"
b = " age is  25"
print(a+b)

# data type boolean
service_running = True
if service_running:
    print("system healthy")

# another example of data type boolean
disk_full = False
if disk_full:
    print("alert")
# nothing prints because condition is false

load = 4
if load > 5:
    print("system is busy")

# program about else condition
load = 4
if load > 4:
    print("system is busy")
else: 
    print("system is normal")

# all 3 conditions
cpu = 80

if cpu > 90:
    print("critical")
elif cpu > 70:
    print("warning")
else:
    print("normal")

# Program on nested condition
cpu = 98
if cpu > 80:
    print("high cpu")
    if cpu > 95:
        print("cpu is critical")


# program on loop
count = 1
while count <= 3:
    print("Ravi")
    count = count +1

i = 1
while i <= 5:
    print("special forces")
    i = i +1

# infinite loop

# using BREAK in loop

count = 1
while True:
    print(count)

    if count == 3:
        break
    count = count +1

# using continue for skipping a step

i = 1
while i <= 5:
    if i == 4:
        i = i +1
        continue
    print(i)
    i = i +1 

# task about infinite loop but stop at 5 using break

i = 1
while True:
    print(i)
    if i == 5:
        break
    i = i +1

# Task 2 print numbers 1-6 but skip 4 using continue

i = 1
while i <= 6:
    if i == 4:
        i = i + 1
        continue
    print(i)

    i = i + 1

# For loop

for i in range(4):
    print("Ravindra")

# Taks 1
for i in range(1,10):
    print("deploy attempt", i)

# Task 2 
apps = ["ravi", "special forces"]

for app in apps:
    print("deploying", app)

# printing numbers from 5 to 1 using range
for i in range(5, 0, -1):
    print(i)

# program on function
def greet():
    print("Hello Tier 1 Operator")
greet()


def love():
    print("a beautiful emotion")
love()

def hello():
    print("Hello Ravindra")
hello()


# calling function using loop
def start():
    print("who dares wins")
for i in range(10):
    start()
# now loop calls functions automatically.
# you don't write manually

servers = ["web1", "web2", "web3", "web4", "web5" ] # here we are calling the function manually

def restart():
    print("Restarting server")

for s in servers:
    restart()

# first parameter function- 

def restart(server):
    print("restarting", server)
    

# program about return value

def add(a, b):
    result = a + b
    return result

total = add(2, 3)

print(total)

# one more return example 

def check_cpu():
    return 90
cpu = check_cpu()
if cpu > 80:
    print("scale system")

# one more task about return

def multiply(a, b):
    return a * b
result = multiply(3, 5)
print(result)

# practice problem 2

def get_status():
    return "running"

status = get_status()

print("service is", status)
