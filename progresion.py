n = int(input('Numero final: '))
n0 = int(input('Numero inicial: '))

s = 0

f = (n-n0+1)*(n0+n)/2
print(f'Resultado formula: {"%d" %f}')

for i in range(n0, n+1):
    s += i

print(f'Resultado sumatorio: {s}')