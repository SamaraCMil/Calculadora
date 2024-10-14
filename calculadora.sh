#!/bin/bash

while true
do
    # Recebendo dois números do usuário
    read -p "Digite o primeiro número: " num1
    read -p "Digite o segundo número: " num2

    # Exibindo opções de operações
    echo "Escolha a operação:"
    echo "1. Adição"
    echo "2. Subtração"
    echo "3. Multiplicação"
    echo "4. Divisão"
    echo "5. Potenciação"
    echo "6. Sair"

    # Recebendo a opção do usuário
    read -p "Digite o número da operação desejada: " opcao

    # Realizando a operação escolhida
    case $opcao in
        1)
            resultado=$(echo "$num1 + $num2" | bc)
            echo "O resultado da adição é: $resultado"
            ;;
        2)
            resultado=$(echo "$num1 - $num2" | bc)
            echo "O resultado da subtração é: $resultado"
            ;;
        3)
            resultado=$(echo "$num1 * $num2" | bc)
            echo "O resultado da multiplicação é: $resultado"
            ;;
        4)
            if [ "$num2" != "0" ]; then
                resultado=$(echo "$num1 / $num2" | bc)
                echo "O resultado da divisão é: $resultado"
            else
                echo "Erro: Divisão por zero não é permitida."
            fi
            ;;
        5)
            resultado=$(echo "$num1 ^ $num2" | bc)
            echo "O resultado da potenciação é: $resultado"
            ;;
        6)
            echo "Saindo da calculadora."
            break
            ;;
        *)
            echo "Opção inválida."
            ;;
    esac
done
