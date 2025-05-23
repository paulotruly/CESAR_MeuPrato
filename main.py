# Cardápio

# Função - OK
# Tratamento de erros e execeções - OK
# CRUD - OK
# Estrutura de dados
# Manipulação de arquivos

# Cardápio

# Função - OK
# Tratamento de erros e exceções - OK
# CRUD - OK
# Estrutura de dados
# Manipulação de arquivos

from selecionar_prato import selecionar_prato

def mostrar_pedidos(pedidos):
    if not pedidos:
        print("Nenhum pedido no momento.")
    else:
        print("\nPedidos atuais:")
        for i, pedido in enumerate(pedidos, 1):
            print(f"{i}. {pedido}")

def salvar_pedido_txt(pedidos, nome_arquivo="pedido_final.txt"):
    with open(nome_arquivo, "w", encoding="utf-8") as f:
        f.write("----- Pedido Final -----\n\n")
        if not pedidos:
            f.write("Nenhum pedido realizado.\n")
        else:
            for i, pedido in enumerate(pedidos, 1):
                f.write(f"{i}. {pedido}\n")
        f.write("\nObrigado pelo pedido! Volte sempre!\n")

def main():
    pedidos = []

    while True:
        print("\nSistema de Pedidos - Escolha uma opção:")
        print("1 - Adicionar novo pedido")
        print("2 - Mostrar pedidos")
        print("3 - Atualizar pedido")
        print("4 - Deletar pedido")
        print("5 - Sair")
        
        escolha = input("Digite a opção desejada: ")

        if escolha == '1':
            prato = selecionar_prato()
            if prato:
                pedidos.append(prato)
                print(f"Pedido '{prato}' adicionado com sucesso!")
            else:
                print("Nenhum prato selecionado, nada foi adicionado.")
        
        elif escolha == '2':
            mostrar_pedidos(pedidos)
        
        elif escolha == '3':
            mostrar_pedidos(pedidos)
            if pedidos:
                try:
                    idx = int(input("Digite o número do pedido que deseja atualizar: "))
                    if 1 <= idx <= len(pedidos):
                        print("Selecione o novo prato para atualizar o pedido:")
                        novo_prato = selecionar_prato()
                        if novo_prato:
                            pedidos[idx - 1] = novo_prato
                            print("Pedido atualizado com sucesso!")
                        else:
                            print("Atualização cancelada. Nenhum prato selecionado.")
                    else:
                        print("Número inválido.")
                except ValueError:
                    print("Digite um número válido.")
        
        elif escolha == '4':
            mostrar_pedidos(pedidos)
            if pedidos:
                try:
                    idx = int(input("Digite o número do pedido que deseja deletar: "))
                    if 1 <= idx <= len(pedidos):
                        pedido_removido = pedidos.pop(idx - 1)
                        print(f"Pedido '{pedido_removido}' removido com sucesso!")
                    else:
                        print("Número inválido.")
                except ValueError:
                    print("Digite um número válido.")
        
        elif escolha == '5':
            print("Saindo do sistema. Obrigado!")
            salvar_pedido_txt(pedidos)  # Salva o arquivo antes de sair
            print("Pedido salvo em 'pedido_final.txt'")
            break
        
        else:
            print("Opção inválida! Por favor, selecione entre 1 e 5.")

if __name__ == "__main__":
    main()

