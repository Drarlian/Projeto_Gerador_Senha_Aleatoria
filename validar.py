def validar_int(texto: str) -> int:
    while True:
        try:
            valor: int = int(input(texto))
        except ValueError:
            print('Digite um valor váliado.')
        else:
            return valor


def validar_caracter(texto: str) -> str:
    while True:
        try:
            caractere: str = str(input(texto)).upper().strip()[0]
        except IndexError:
            print('Digite um caractere válido.')
        else:
            if caractere == 'S' or caractere == 'N':
                return caractere
            else:
                print('Digite um caractere válido.')
