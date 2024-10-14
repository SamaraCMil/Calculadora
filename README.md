
# Calculadora Simples em Python

## Descrição
Este projeto é uma calculadora simples desenvolvida em Python que permite ao usuário realizar cinco operações matemáticas: adição, subtração, multiplicação, divisão e potenciação entre dois números. O código continua a executar até que o usuário escolha a opção de sair.

## Explicação do Código (Python)
O código implementado no arquivo **calculadora.sh** realiza operações matemáticas básicas de forma interativa com o usuário. Abaixo está a explicação detalhada de cada parte do código:

```python
# Calculadora com 5 operações

while True:
    # Recebendo dois números do usuário
    num1 = float(input("Digite o primeiro número: "))  # Recebe o primeiro número e o converte para ponto flutuante
    num2 = float(input("Digite o segundo número: "))   # Recebe o segundo número e o converte para ponto flutuante

    # Exibindo opções de operações
    print("Escolha a operação:")  # Mostra o menu de operações
    print("1. Adição")            # Opção para somar
    print("2. Subtração")         # Opção para subtrair
    print("3. Multiplicação")     # Opção para multiplicar
    print("4. Divisão")           # Opção para dividir
    print("5. Potenciação")       # Opção para calcular a potência
    print("6. Sair")              # Opção para sair do programa

    # Recebendo a opção do usuário
    opcao = input("Digite o número da operação desejada: ")  # Lê a opção escolhida pelo usuário

    # Realizando a operação escolhida
    if opcao == "1":  # Caso o usuário escolha a adição
        resultado = num1 + num2  # Realiza a soma dos dois números
        print("O resultado da adição é:", resultado)  # Exibe o resultado da soma

    elif opcao == "2":  # Caso o usuário escolha a subtração
        resultado = num1 - num2  # Realiza a subtração dos dois números
        print("O resultado da subtração é:", resultado)  # Exibe o resultado da subtração

    elif opcao == "3":  # Caso o usuário escolha a multiplicação
        resultado = num1 * num2  # Realiza a multiplicação dos dois números
        print("O resultado da multiplicação é:", resultado)  # Exibe o resultado da multiplicação

    elif opcao == "4":  # Caso o usuário escolha a divisão
        if num2 != 0:  # Verifica se o divisor não é zero (para evitar erro de divisão por zero)
            resultado = num1 / num2  # Realiza a divisão dos dois números
            print("O resultado da divisão é:", resultado)  # Exibe o resultado da divisão
        else:
            print("Erro: Divisão por zero não é permitida.")  # Exibe mensagem de erro caso o divisor seja zero

    elif opcao == "5":  # Caso o usuário escolha a potenciação
        resultado = num1 ** num2  # Realiza a potenciação (num1 elevado a num2)
        print("O resultado da potenciação é:", resultado)  # Exibe o resultado da potenciação

    elif opcao == "6":  # Caso o usuário escolha sair
        print("Saindo da calculadora.")  # Exibe mensagem de saída
        break  # Encerra o loop e finaliza o programa

    else:
        print("Opção inválida.")  # Exibe mensagem de erro caso a opção seja inválida





