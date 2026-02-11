#Formato para texto
#Los siguientes metodos de formato valen para todo tipo de texto, no es exclusivo del metodo print
var = 'variable'
print(f'Texto con {var} en el propo texto')
print('Otra manera de dar formato al texto {}'.format(var))
print("My name is {fname}, I'm {age}".format(fname = "John", age = 36)) #Se pueden crear las variables dentro del .format()
print("Pi: {:.3f}".format(3.141592)) #Formato que condiciona el numero de digitos a usar
#Desglose del formato:
# : Sirve para decirle al formato que el numero tmb esta formateado
# .Xf Siendo X el numero de decimales a mostrar, la f se usa si es un numero tipo float
print("Pi: {:05d}".format(313))
#Es lo mismo que:
print(f'Pi: {313:05d}')
# 0Xd Sirve para añadir 0 hasta llegar al numero de decimales, si supera de por si este numero no hara nada
print("Pi: {:5d}".format(313))
# Xd Si no usamos el 0 simplemente movera X caracteres el numero
print("Lenguaje: {:s}".format('Python'))
# :s significa que el format cambiara el tipo del objeto a str
print("Lenguaje: {:.3s}".format('Python'))
# :.Xs significa que el texto cogera los primeros 3 caracteres