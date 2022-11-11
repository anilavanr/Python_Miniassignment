
import cmath

a = int(input("Enter the number: "))
b = int(input("Enter the number: "))
c = int(input("Enter the number: "))

d = (b**2) - (4*a*c)

Answer1 = (-b-cmath.sqrt(d))/(2*a)
Answer2 = (-b+cmath.sqrt(d))/(2*a)

print('The solution are {0} and {1}'.format(Answer1,Answer2))