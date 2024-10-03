def verificar_qtd_a(entrada: str):
    cont = 0
    for i in entrada.lower():
        if i == "a":
            cont += 1
    return cont

def mostrar_mensagem(resultado:int):
    if resultado>0:
        print(f"A string possui {resultado} a's")
    else:
        print(f"A string NAO possui a's")

def main():
    print("Verificador de a's")
    print("Digite -1 para finalizar")
    while True:
        # entrada = input("\nDigite uma palavra ou frase:")
        entrada = 'PnAEuMa'
        if entrada.isnumeric() or entrada == "-1":
            break
        resultado = verificar_qtd_a(entrada)
        mostrar_mensagem(resultado)
        
        if entrada == "PnAEuMa":
            break
    print("------------------------")
    print("Programa finalizado")


if __name__ == "__main__":
    main()