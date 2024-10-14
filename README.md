# Calculadora Simples em Shell Script

## Descrição
Este script implementa uma calculadora simples utilizando Shell Script (Bash). O programa permite ao usuário realizar cinco operações matemáticas básicas (adição, subtração, multiplicação, divisão e potenciação) com dois números. A calculadora permanece em execução até que o usuário escolha a opção de sair.

## Explicação do Código

O script funciona em um loop contínuo (`while true`) até que o usuário escolha a opção de encerrar o programa. A seguir está a explicação detalhada de cada parte:

```bash
#!/bin/bash
```

1. **Shebang**: Define o interpretador do script como `bash`. Todo o script será executado usando o Bash Shell.
```bash
while true
do
```

2. **Loop Infinito**: O comando while true inicia um loop que repete continuamente até que o usuário decida sair da calculadora.
```
# Recebendo dois números do usuário
       read -p "Digite o primeiro número: " num1
       read -p "Digite o segundo número: " num2
```
3. **Recebimento dos Números**: O comando read solicita que o usuário insira dois números `(num1 e num2)`, que serão utilizados nas operações matemáticas.
```
 # Exibindo opções de operações
    echo "Escolha a operação:"
    echo "1. Adição"
    echo "2. Subtração"
    echo "3. Multiplicação"
    echo "4. Divisão"
    echo "5. Potenciação"
    echo "6. Sair"
```

4. **Exibição do Menu de Operações**: As opções de operações matemáticas são exibidas ao usuário usando o comando echo.
```
    # Recebendo a opção do usuário
    read -p "Digite o número da operação desejada: " opcao
```
5. **Escolha da Operação**: O usuário insere o número correspondente à operação que deseja realizar.
```
    # Realizando a operação escolhida
    case $opcao in
        1)
            resultado=$(echo "$num1 + $num2" | bc)
            echo "O resultado da adição é: $resultado"
            ;;

```
6. **Adição**: Se o usuário escolher a opção 1, o programa realiza a soma de `num1` e `num2` usando `bc` (um calculador de precisão arbitrária no Bash) e exibe o resultado.
```
        2)
            resultado=$(echo "$num1 * $num2" | bc)
            echo "O resultado da multiplicação é: $resultado"
            ;;

```
7. **Subtração**: Se o usuário escolher a opção 2, o programa subtrai `num2` de `num1` e exibe o resultado.
```
     3)
            resultado=$(echo "$num1 * $num2" | bc)
            echo "O resultado da multiplicação é: $resultado"
            ;;
```
8. **Multiplicação**: A multiplicação de num1 por num2 é realizada e o resultado é mostrado.
