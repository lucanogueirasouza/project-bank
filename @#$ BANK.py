saldo = 0
extrato = []
quantidade_de_saques = 0

while True:
    escolha = int(input(
        """
======== MENU - BANCO @#$ ========

1. Sacar
2. Depositar
3. Ver Extrato 
4. Avançar dia
5. Sair

Escolha: """
    ))

    if escolha == 1:
        if quantidade_de_saques < 3:
            try:
                sacar = float(input(
                    "Digite o valor que deseja sacar: "
                    ))

                if saldo < sacar:
                    print(
                        "Você não tem saldo suficiente para sacar tal valor. Tente novamente."
                        )
                    continue

                if sacar > 500:
                    print(
                        "O valor máximo por vez de saque é de R$500. Tente novamente."
                        )
                    continue

                saldo_antigo = saldo
                saldo -= sacar
                quantidade_de_saques += 1
                extrato.append(
                    f"Saque - Valor antigo: R$ {saldo_antigo:.2f}, Valor novo: R$ {saldo:.2f}"
                    )
                print(
                    f"Valor sacado: R$ {sacar:.2f}"
                    )

            except ValueError:
                print("Digite um valor válido.")
                continue

        else:
            print("Você atingiu o limite de 3 saques por dia.")
            continue

    elif escolha == 2:
        try:
            depositar = float(input("Digite o valor que deseja depositar: "))
            saldo_antigo = saldo
            saldo += depositar
            extrato.append(
                f"Depósito - Valor antigo: R$ {saldo_antigo:.2f}, Valor novo: R$ {saldo:.2f}"
                )
            print(
                f"Valor depositado: R$ {depositar:.2f}"
                )
        except ValueError:
            print(
                "Digite um valor válido."
                )

    elif escolha == 3:
        print(
            "\n====== EXTRATO ======"
            )
        if extrato:
            for operacao in extrato:
                print(operacao)
        else:
            print(
                "Nenhuma operação realizada."
                )
        print(
            f"Saldo atual: R$ {saldo:.2f}"
            )
        print(
            "======================\n"
            )

    elif escolha == 4:
        quantidade_de_saques = 0
        print(
            "Novo dia iniciado. Limite de saques resetado."
            )

    elif escolha == 5:
        print(
            "Obrigado por utilizar o Banco @#$. Até logo!"
            )
        break

    else:
        print(
            "Opção inválida. Tente novamente."
            )
