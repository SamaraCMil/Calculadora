# -*- coding: utf-8 -*-
"""Calculadora.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1rvB-OJBTrh6cpuQpsBd3H3yKNqUyvnh-
"""

# Calculadora com 5 operações
while True:
          # Recebendo dois números do usuario
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número:"))

        # Exibindo Opçoes de opereções
        print("Escolha a operação:")
        print("1. Adição")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão")
        print("5. Potenciação")
        print("6. Sair")

        # Recebendo a opção do usuário
        opcao = input("Digite o número da operação desejada: ")

        # Recebdno a operação escolhida
        if opcao == "1":
            resultado = num1 + num2
            print("O resultado da adição é:", resultado)
        elif opcao == "2":
            resultado = num1 - num2
            print("O resultado da subtração é:", resultado)
        elif opcao == "3":
            resultado = num1 * num2
            print("O resultado da multiplicação é:", resultado)
        elif opcao == "4":
            if num2 != 0:
                resultado = num1 / num2
                print("O resultado da divisão é:", resultado)
            else:
                print("Erro: Divisão por zero não é permitida.")
        elif opcao == "5":
            resultado = num1 ** num2
            print("O resultado da potenciação é:", resultado)
        elif opcao == "6":
            print("Saindo da calculadora.")
            break