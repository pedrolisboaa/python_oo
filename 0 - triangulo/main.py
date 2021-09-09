from triangulo import Triangulo

print('Enter the measures of triangle X:')
a = float(input())
b = float(input())
c = float(input())

triangulo1 = Triangulo(a, b, c)

print('Enter the measures of triangle Y:')
d = float(input())
e = float(input())
f = float(input())

triangulo2 = Triangulo(d, e, f)

print(triangulo1.area())
print(triangulo2.area())
