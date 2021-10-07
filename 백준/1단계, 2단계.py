'''
print("Hello, World!")
print("Hello\nWorld!")
print("\    /\ \n )  ( ')\n(  /  )\n \(__)|")
print('|\_/|\n|q p|   /}\n( 0 )"""\ \n|"^"`    | \n||_/=\\\__|')
'''

A = int(input(""))
B = int(input(""))
C = A+B
print(C)


a, b = map(int, input().split() )
print(a+b)
print(a-b)
print(a*b)
print(a//b)
print(a%b)

A,B,C = map(int, input().split() )
print((A+B)%C)
print(((A%C)+(B%C))%C)
print((A*B)%C)
print(((A%C)*(B%C))%C)


a,b = map(int, input().split())


b1 = b%10
b2 = (b%100)//10
b3 = b//100

print(a*b1)
print(a*b2)
print(a*b3)
print(a*b)


a = int(input())


if a%4 != 0:
    print("0")

elif a%100 != 0:
    print("1")

elif a%400 == 0:
    print("1")

else:
    print("0")

'''

일단 4의 배수 

1) 4의 배수 중 100의 배수x

or 

2) 400의 배수 

'''

x = int(input())
y = int(input())

if x > 0 and y > 0:
    print("1")

elif x < 0 and y > 0:
    print("2")

elif x < 0 and y < 0:
    print("3")

elif x > 0 and y < 0:
    print("4")

else:
    print("Not on Quadrant")



H, M = map(int, input().split())

if H != 0:
    if M < 45:
        print(H-1,M+15)
    
    else:
        print(H,M-45)


else:
    if M < 45:
        print("23",M+15)

    else:
        print("0",M-45)
