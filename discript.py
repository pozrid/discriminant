a = float(input())
b = float(input())
c = float(input())
D = b**2 -4*a*c
print('Дискриминант =',D)
if D < 0:
    print('Нельзя >:(')
elif D > 0:
    print('x1 =',(-b - D**0.5)/(2*a))
    print('x2 =', (-b + D**0.5)/(2*a))
else:
    print('x =',-b/2*a)
    