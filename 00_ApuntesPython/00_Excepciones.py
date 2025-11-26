try:
    print
except Exception:
    print()
except ValueError:
    print()

try:
    print
except: # No hace falta poner una excepcion especifica
    print()