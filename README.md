# Sistema Bancário em Python | Python Banking System

BR - Projeto extremamente básico que desenvolvi apenas para entregar em um bootcamp que estou realizando.

US - Extremely basic project that I developed just to deliver in a bootcamp that I am performing.
#

Este é um sistema bancário simples criado em Python, que permite ao usuário:

- Sacar valores com regras de limite
- Depositar quantias na conta
- Visualizar extrato com histórico de operações
- Avançar o dia e resetar o limite de saques
- Encerrar o programa

This is a simple banking system built in Python, which allows the user to:

- Withdraw money with daily limits
- Deposit amounts into the account
- View transaction history
- Advance the day and reset withdrawal limits
- Exit the program

---

## Funcionalidades | Features

- Limite de 3 saques por dia  
- Valor máximo de saque: R$500 por operação  
- Registro de cada operação no extrato (depósito e saque)  
- Exibição do saldo atual no extrato  
- Menu interativo baseado em terminal  
- Opção para reiniciar os limites ao "avançar o dia"  

- Daily withdrawal limit: 3 times  
- Max withdrawal per operation: R$500  
- Deposit and withdrawal history tracking  
- Balance displayed in the statement  
- Terminal-based interactive menu  
- Option to reset limits by "advancing the day"

---

## Tecnologias | Technologies

- Python 3.x
- Biblioteca padrão (sem bibliotecas externas)

---

## Como usar | How to use

1. Salve o código como `banco.py`  
2. Execute no terminal:  
   ```bash
   python banco.py
