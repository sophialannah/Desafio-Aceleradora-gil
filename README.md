Guia para Rodar o Projeto
Tecnologias Utilizadas
Python: Plataforma de execução para construir a aplicação.
JSON: Para persistência dos dados em um arquivo local chamado inventario.json.
Funções básicas do Python: Para manipulação do inventário e interação com o usuário via terminal.
Como Rodar o Projeto
Pré-requisitos
Certifique-se de ter o Python instalado. Você pode verificar a instalação com o comando:

bash
Copiar código
python --version
Caso o Python não esteja instalado, baixe e instale a partir do site oficial do Python.

Passos para Rodar
Clone ou copie o código para o seu ambiente local.

Crie um arquivo inventario.json no mesmo diretório do script:

Se o arquivo não existir, ele será criado automaticamente após a primeira execução.
Abra o terminal e navegue até o diretório do projeto:

bash
Copiar código
cd <caminho_para_diretorio>
Execute o script:

bash
Copiar código
python app.py
Exemplo:

bash
Copiar código
python app.py
Funcionalidades Disponíveis
Após rodar o script, você verá o menu principal com as seguintes opções:

Adicionar Produto: Permite adicionar novos produtos ao inventário com os campos:
Nome
Categoria
Quantidade
Preço
Listar Produtos: Exibe todos os produtos cadastrados em formato tabular, com:
ID
Nome
Categoria
Quantidade
Preço
Atualizar Produto: Atualiza as informações de um produto existente, identificado pelo ID.
Excluir Produto: Remove um produto do inventário, confirmando antes a exclusão.
Buscar Produto: Busca produtos pelo ID ou nome (aceita parte do nome).
Sair: Encerra a aplicação.
Persistência de Dados
Todos os dados são salvos no arquivo inventario.json. Assim, ao reiniciar a aplicação, as informações já cadastradas serão carregadas automaticamente.