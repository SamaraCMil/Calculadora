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
8. **Multiplicação**: A multiplicação de `num1` por `num2` é realizada e o resultado é mostrado.
```
        4)
            if [ "$num2" != "0" ]; then
                resultado=$(echo "$num1 / $num2" | bc)
                echo "O resultado da divisão é: $resultado"
            else
                echo "Erro: Divisão por zero não é permitida."
            fi
            ;;

```
9. **Divisão**: Verifica se o divisor (`num2`) é diferente de zero antes de realizar a divisão. Caso contrário, exibe uma mensagem de erro indicando que a divisão por zero não é permitida.
```
        5)
            resultado=$(echo "$num1 ^ $num2" | bc)
            echo "O resultado da potenciação é: $resultado"
            ;;

```
10. **Potenciação**: O programa calcula `num1` elevado à potência de `num2` e exibe o resultado.
```
        6)
            echo "Saindo da calculadora."
            break
            ;;

```

11. **Sair**: Se o usuário escolher a opção 6, o programa encerra o loop e exibe a mensagem "Saindo da calculadora".
```
        *)
            echo "Opção inválida."
            ;;
    esac
done
```

12. **Opção Inválida**: Caso o usuário insira um número diferente das opções disponíveis (1 a 6), o programa exibe uma mensagem de erro indicando que a opção é inválida.

# Como Executar o Script

1. **Salvar o arquivo**: Crie um arquivo chamado `calculadora.sh` e cole o código acima.
2. **Tornar o arquivo executável**: Altere as permissões do arquivo para torná-lo executável com o seguinte comando:
```
chmod +x calculadora.sh
```
3. **Executar o script**: Para rodar o script, use o comando:
```
./calculadora.sh
```
4.**Interagir com a calculadora**: Digite os dois números e escolha a operação desejada. A calculadora exibirá o resultado e permitirá que você realize mais operações até escolher a opção de sair.
