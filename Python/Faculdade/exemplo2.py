import math

U0= 1200 
t= 6
k= 0.10

U_t= U0 *math.exp(k*t)

print (f"Numero estimado de usuarios apos {t} meses:{U_t:2f}")