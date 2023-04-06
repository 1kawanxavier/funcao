def verificar_palindromo(texto):
    texto = texto.lower().replace(" ","")
    return texto == texto[::-1]
    
texto = "socorram me subi no onibus em marrocos"
if  verificar_palindromo(texto):
    print(texto, "é um palindromo")
else: 
    print(texto, "não é um palindromo")