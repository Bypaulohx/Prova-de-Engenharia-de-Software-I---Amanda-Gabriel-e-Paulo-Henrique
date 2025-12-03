📊 Calculadora de Média de Notas Aprimorada

Este projeto contém um script Python (calculadora_complexa_notas.py) desenvolvido para calcular a média aritmética de uma lista de notas ou pontuações, incorporando boas práticas de programação e robustez no tratamento de dados.

📝 Origem e Melhoria do Código

O código original para o cálculo da média de notas foi baseado em exercícios e conceitos retirados de aulas iniciais de programação Python.

O script original foi aprimorado para o módulo atual, implementando as seguintes melhorias:

Modularidade: A lógica principal de cálculo foi isolada em uma função reutilizável (calcular_media_ponderada) que aceita qualquer lista de notas como argumento.

Tratamento de Erros: Adição de verificações para:

Lista Vazia: Evita a divisão por zero.

Dados Não-Numéricos: Garante que apenas números sejam somados, retornando uma mensagem de erro clara caso encontre texto ou dados inválidos na lista.

Clareza de Variáveis: Uso de nomes de funções e variáveis descritivos, como lista_pontuacoes e somatorio_pontuacoes.

Demonstração: Uma função de exibição (exibir_resultado_processamento) demonstra o uso do módulo em cenários reais, incluindo exemplos de sucesso e falha (erros).

💡 Como Executar

Salve o arquivo calculadora_complexa_notas.py.

Execute-o diretamente no terminal:

python calculadora_complexa_notas.py


🚀 Fluxo de Trabalho Git (Controle de Versão)

O desenvolvimento deste projeto segue o fluxo de trabalho Git padrão, conforme detalhado no arquivo guia_git_passo_a_passo.md. As etapas essenciais que garantiram a adição e o aprimoramento deste código foram:

Criação do Repositório (git init): Início do rastreamento de mudanças.

Desenvolvimento em Branch: Criação de uma branch isolada (ex: feature/melhoria-funcional) para trabalhar na refatoração e nos aprimoramentos.

Commits: Registro das alterações incrementais com mensagens claras.

Pull Request (PR): Envio da branch para revisão e posterior mesclagem na branch principal (main), garantindo a qualidade do código antes da integração final.
