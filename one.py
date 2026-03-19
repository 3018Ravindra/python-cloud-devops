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
cpu = 90
if cpu > 80:
    print("high cpu")
    if cpu > 95:
        print("cpu is critical")

        