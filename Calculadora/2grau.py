import math
A = int(input('digite o valor de A:'))
B = int(input('digite o valor de B:'))
C = int(input('digite o valor de C:'))
D = B**2 - (4*A*C)
print('delta=',D)
user = str(input('digite (s) caso tenha entendido ou (n) para ver passo a passo: '))
if (user == 's' ): 
  x1 = (-B + math.sqrt(D))/(2*A) 
  x2 = (-B - math.sqrt(D))/(2*A)
  print("x1 =",x1,'x2 =',x2)
else:
  print('b**2 =',B**2)
  print('4*A*C =',4*A*C)
  print('delta = B**2 - 4AC')
  print('delta=',D)
  x1 = (-B + math.sqrt(D))/(2*A) 
  x2 = (-B - math.sqrt(D))/(2*A)
  print("x1 =",x1,'x2 =',x2)
  user2 = str(input('digite (s) caso tenha entendidoo valor de x1/x2 ou (n) para ver passo a passo:'))
  if (user2 == 's'):
    print('espero ter conseguido responder sua equação')
  else:
    print('raiz de delta=',math.sqrt(D))
    print('x1=-B + raiz de delta / 2*A')
    print('x1=',x1)
    print('x2=-B - raiz de delta / 2*A')
    print('x2=',x2)
    print('espero ter conseguido responder sua equação')