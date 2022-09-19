strNumero = input("Digite um número inteiro: ")
numero = int(strNumero)
conta = numero // 10
strConta = str(conta)
comprimento = len(strConta)
valorDezena = strConta[comprimento-1]
print ("O dígito das dezenas é", valorDezena)