def concat(cad1 , cad2):
    return cad1 + " " + cad2

def contarCar(cad, c):
    if c == "":
        return 0
    return cad.count(c)

def mayus(cad):
    return cad.capitalize()


x = input('Introduce una palabra (-1 o end para terminar) -> ')

frase = ""

while x != '-1' and x != 'end':
    frase = concat(frase, x)
    x = input('Introduce una palabra (-1 o end para terminar) -> ')

fraseMayus = mayus(frase)

print(f'La frase con la primera letra en mayúscula es: {fraseMayus}')

vocales = ['a', 'e', 'i', 'o', 'u']

for vocal in vocales:
    print(f'La vocal "{vocal}" aparece {contarCar(frase, vocal)} veces en la frase.')
