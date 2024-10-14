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

