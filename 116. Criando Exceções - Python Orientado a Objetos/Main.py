class ISWRONG(Exception):
    pass

def testar():
    raise ISWRONG("ERROR :: 51")

try:
    testar()
except ISWRONG as error:
    print(f'erro:{error}')

