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

