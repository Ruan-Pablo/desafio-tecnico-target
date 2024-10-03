class Fibonacci:
    def __init__(self, numero) -> None:
        self.ant = 0
        self.atual = 1
        self.proximo = 0
        self.numero = numero

    def verificar(self):
        if self.numero in [0, 1]:  # se (0 e 1) eh valido
            return True

        while self.proximo < self.numero:
            self.proximo = self.atual + self.ant
            if self.proximo == self.numero:
                return True
            self.ant = self.atual
            self.atual = self.proximo
        return False


def mostrar_mensagem(valor):
    if valor:
        return "O valor informado pertence a sequência Fibonacci."
    else:
        return "O valor informado NAO pertence a sequência de Fibonacci."


def main():
  print("Verificador de pertencimento da sequencia Fibonacci")
  print("Digite -1 para finalizar")

  while True:
      numero = input("Digite um numero:") # o input da uns probleminhas, entao foi necessario utilizar o colab
      if numero == "-1":
          break
      if not numero.isnumeric():
          print("Digite um numero valido!!")
          continue

      numero = int(numero)

      fibonacci = Fibonacci(numero)
      resultado = fibonacci.verificar()
      print(mostrar_mensagem(resultado))

  print("------------------------")
  print("Programa finalizado")

if __name__ == "__main__":
    main()
