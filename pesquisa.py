# Empresa-TudoWeb# ==========================================================
# Programa de Pesquisa de Satisfação - Empresa TudoWeb
# Descrição: Coleta dados de satisfação de clientes utilizando FOR.
# ==========================================================

def main():
    # Defina o total de entrevistados. 
    # Nota: Altere para 10 caso queira realizar testes rápidos conforme o item 8.
    TOTAL_ENTREVISTADOS = 50

    # Contadores para as estatísticas exigidas
    qtd_excelente = 0
    qtd_bom = 0
    qtd_ruim = 0

    print("=" * 50)
    print("        PESQUISA DE SATISFAÇÃO - TUDOWEB")
    print("=" * 50)

    # Estrutura de repetição FOR para coletar os dados dos entrevistados
    for i in range(1, TOTAL_ENTREVISTADOS + 1):
        print(f"\n--- Entrevistado {i} de {TOTAL_ENTREVISTADOS} ---")
        
        # Coleta do nome e idade
        nome = input("Digite o nome do entrevistado: ")
        
        while True:
            try:
                idade = int(input("Digite a idade do entrevistado: "))
                if idade > 0:
                    break
                print("Por favor, digite uma idade válida maior que zero.")
            except ValueError:
                print("Entrada inválida! Digite apenas números inteiros para a idade.")

        # Coleta da opinião com validação
        print("\nTabela de Opiniões:")
        print("  [1] EXCELENTE")
        print("  [2] BOM")
        print("  [3] RUIM")
        
        opiniao = 0
        while opiniao not in [1, 2, 3]:
            try:
                opiniao = int(input("Digite o código da sua opinião (1, 2 ou 3): "))
                if opiniao not in [1, 2, 3]:
                    print("Opção inválida! Escolha entre 1, 2 ou 3.")
            except ValueError:
                print("Entrada inválida! Digite um número inteiro correspondente.")

        # Estrutura de decisão para contabilizar as respostas
        if opiniao == 1:
            qtd_excelente += 1
        elif opiniao == 2:
            qtd_bom += 1
        elif opiniao == 3:
            qtd_ruim += 1

    # Exibição dos resultados finais solicitados pela atividade
    print("\n" + "=" * 50)
    print("              RESULTADO FINAL DA PESQUISA")
    print("=" * 50)
    print(f"Total de entrevistados participantes: {TOTAL_ENTREVISTADOS}")
    print(f"a) Quantidade de respostas 'EXCELENTE': {qtd_excelente}")
    print(f"b) Quantidade de respostas 'RUIM': {qtd_ruim}")
    print(f"(Respostas 'BOM' registradas: {qtd_bom})")
    print("=" * 50)

if __name__ == "__main__":
    main()
