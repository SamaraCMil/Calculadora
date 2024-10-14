# Calculadora Simples em Python

## Descrição
Este código implementa uma calculadora simples em Python, que permite ao usuário realizar cinco operações matemáticas básicas (adição, subtração, multiplicação, divisão e potenciação) com dois números. O programa continua executando até que o usuário escolha a opção de sair.

## Explicação do Código

O código é estruturado para funcionar em um loop contínuo que somente será interrompido caso o usuário escolha a opção de sair. Abaixo está a explicação detalhada de cada parte:

```python
# Calculadora com 5 operações
while True:
    # Recebendo dois números do usuário
    num1 = float(input("Digite o primeiro número: "))  # Recebe o primeiro número e o converte para ponto flutuante
    num2 = float(input("Digite o segundo número: "))   # Recebe o segundo número e o converte para ponto flutuante
```

1. **Loop infinito**: O programa usa `while True` para repetir indefinidamente o processo, até que o usuário decida sair.
2. **Recepção dos números**: O programa solicita ao usuário dois números, convertendo-os em valores de ponto flutuante (`float`) para garantir que operações com decimais sejam possíveis.
```
    # Exibindo opções de operações
    print("Escolha a operação:")  # Exibe as opções disponíveis para o usuário
    print("1. Adição")            # Opção 1: Adição
    print("2. Subtração")         # Opção 2: Subtração
    print("3. Multiplicação")     # Opção 3: Multiplicação
    print("4. Divisão")           # Opção 4: Divisão
    print("5. Potenciação")       # Opção 5: Potenciação
    print("6. Sair")              # Opção 6: Encerrar o programa
```
- Explicação: Ao selecionar a opção "6", o programa imprime uma mensagem de despedida e interrompe o loop com o comando break, encerrando o funcionamento da calculadora.

3. **Exibição do menu de operações**: O programa exibe um menu com cinco opções de operações matemáticas (adição, subtração, multiplicação, divisão, potenciação) e uma opção de saída.
python
```
    # Recebendo a opção do usuário
    opcao = input("Digite o número da operação desejada: ")  # O usuário escolhe a operação
```
4. **Escolha da operação**: O usuário escolhe qual operação matemática deseja realizar inserindo o número correspondente.
```
  # Realizando a operação escolhida
    if opcao == "1":  # Caso o usuário escolha adição
        resultado = num1 + num2  # Realiza a adição dos dois números
        print("O resultado da adição é:", resultado)  # Exibe o resultado da adição
    elif opcao == "2":  # Caso o usuário escolha subtração
        resultado = num1 - num2  # Realiza a subtração dos dois números
        print("O resultado da subtração é:", resultado)  # Exibe o resultado da subtração
    elif opcao == "3":  # Caso o usuário escolha multiplicação
        resultado = num1 * num2  # Realiza a multiplicação dos dois números
        print("O resultado da multiplicação é:", resultado)  # Exibe o resultado da multiplicação

```

