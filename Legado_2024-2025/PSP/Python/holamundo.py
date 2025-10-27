#comentario de linea
"""
Comentario multilinea, similar al javadoc
"""
'''
tmb puedes usar esto
'''

a,b = 1,2 #de esta manera se da valores a varias variables a la vez
#---------------------------------------clases---------------------------------------
integer = 1
flotante = 0.1
string = 'hola'
string = "Hola"
booleano = True #obligatorio capital
booleano = a < b

int(booleano)#convierte a integer
float(integer)#convierte a float
bool(integer)#convierte a booleano
str(booleano)#convierte a string
type(a)#dice la clase

print(a, b)

if 0 <= a > 5:
    print("dentro del if")
    if a < 3:
        print("dentro del 2 if")
    else:
        print("else del 2 if")
print("Fuera del if")

print ("for")
for i in range (3,0,-1): #(valor inicial, valor final(no incluidon), incremento)no se puede hacer un limite incluyendo, hay que hacer un if dentro del)for y hacer un break
    print(i)
print ("for")
for i in range (0,3): #puedes no poner el incremento y lo tratara como 1
    print(i)
print ("while")
while a < b :
    a+=1
    print(a)

x = input('Introduce tu nombre:')#por defecto recoje un string
print('Hola me llamo {} y tengo {}'.format(x,21))
print('Hola me llamo {}'.format(x))
pi = 31.141592
print('Py: {:.3f}'.format(pi))

l = [1,2,3,4,5,6]
print('len:'+len(l))
for i,j in enumerate (l+l):
    print(l)
print('len:'+len(l))