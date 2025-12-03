def calcular_media_ponderada(lista_pontuacoes):
    """
    Calcula a média aritmética de uma lista de pontuações.

    Parâmetros:
    - lista_pontuacoes (list): Uma lista de números (inteiros ou floats)
      representando as notas obtidas.

    Retorna:
    - float: O valor da média calculada.
    - str: Uma mensagem de erro, se a lista estiver vazia.
    """
    
    # 1. Validação de dados de entrada: Verifica se a lista não está vazia.
    if not lista_pontuacoes:
        return "Erro: A lista de pontuações está vazia. Impossível calcular a média."

    somatorio_pontuacoes = 0.0

    for valor in lista_pontuacoes:
        try:
            somatorio_pontuacoes += float(valor)
        except ValueError:
            return f"Erro: O valor '{valor}' na lista não é um número válido."

    quantidade_elementos = len(lista_pontuacoes)
    media_final = somatorio_pontuacoes / quantidade_elementos

    return media_final

def exibir_resultado_processamento():
    """
    Função principal que demonstra o uso da calculadora de média com diferentes conjuntos de dados.
    """
    # Exemplo 1: Lista de notas padrão
    notas_aluno_a = [7.5, 8.0, 9.2, 6.8]
    media_a = calcular_media_ponderada(notas_aluno_a)
    print(f"--- Processamento Aluno A ---")
    print(f"Notas registradas: {notas_aluno_a}")

    if isinstance(media_a, float):
        print(f"Resultado: A média final é {media_a:.2f}")
    else:
        print(f"Resultado: {media_a}")


    print("\n" + "="*30 + "\n")


    # Exemplo 2: Lista vazia (Teste de tratamento de erro)
    notas_aluno_b = []
    media_b = calcular_media_ponderada(notas_aluno_b)
    print(f"--- Processamento Aluno B (Teste de Erro) ---")
    print(f"Notas registradas: {notas_aluno_b}")
    print(f"Resultado: {media_b}")


    print("\n" + "="*30 + "\n")


    # Exemplo 3: Lista com um valor não-numérico
    notas_aluno_c = [10, 8, "dez", 5]
    media_c = calcular_media_ponderada(notas_aluno_c)
    print(f"--- Processamento Aluno C (Teste de Erro) ---")
    print(f"Notas registradas: {notas_aluno_c}")
    print(f"Resultado: {media_c}")


if __name__ == "__main__":
    exibir_resultado_processamento()