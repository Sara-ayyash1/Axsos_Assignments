#1
def a():
    return 5
print(a()) # The output is 5


#2
def a():
    return 5
print(a()+a()) # The output is 10


#3
def a():
    return 5
    return 10 #The line after return in Func is unreachable
print(a()) # The output is 5


#4
def a():
    return 5
    print(10) #The line after return in Func is unreachable
print(a()) # The output is 5


#5
def a():
    print(5)

x = a() # The output is 5 
print(x) # The output is none because Function a isn't return value


#6
def a(b,c):
    print(b+c)
print(a(1,2) + a(2,3)) # The output is print  3 then 5 then give error because Function a isn't return value so we cant NoneType + NoneType


#7
def a(b,c):
    return str(b)+str(c)
print(a(2,5)) # The output is print 25


#8
def a():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7 # The line after return in Func is unreachable

print(a()) # The output is print 100 then return 10


#9
def a(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3 # The line after return in Func is unreachable

print(a(2,3)) # The output is print 7
print(a(5,3)) # The output is print 14
print(a(2,3) + a(5,3)) # The output is print 21


#10
def a(b,c):
    return b+c
    return 10 # The line after return in Func is unreachable

print(a(3,5)) # The output is print 8


#11
b = 500 # Global Variable
print(b) # The output is print 500
def a():
    b = 300 # Local Variable
    print(b) 

print(b) # The output is print 500 
a() # The output is print 300
print(b) # The output is print 500 =>Because the 'b' inside the function was deleted as soon as the function finished so the global 'b' outside remains unchanged.


#12
b = 500
print(b) # The output is print 500
def a():
    b = 300
    print(b)
    return b

print(b) # The output is print 500
a() # The output is print 300 
print(b) # The output is print 500


#13
b = 500
print(b) # The output is print 500
def a():
    b = 300
    print(b)
    return b

print(b) # The output is print 500
b=a() # The output is print 300 ,return 300 and store it in b
print(b) # The output is return 300


#14
def a():
    print(1)
    b()
    print(2)

def b():
    print(3)

a() # The output is print 1 then 3 then 2



#15
def a():
    print(1)
    x = b()
    print(x)
    return 10

def b():
    print(3)
    return 5

y = a() #  print 1 then 3 then 5
print(y) # The output is 10