# web-crawler-desafio-turivius

### :memo: Sobre a aplicação

O desafio consiste em criar um programa que, a partir de uma query, faz uma pesquisa na wiki da distribuição Arch Linux (https://wiki.archlinux.org/) e devolve a primeira página encontrada, em plain text, ao usuário.

### :bookmark_tabs: **Features**

- **Interface CLI:** Tratamento e execução apenas por linha de comando, recebendo um único argumento (--query/q)
- **Aviso quando a página não foi encontrada:** Uma simples mensagem de "not found".
- **Retorno da página completa, em plain text.:** Ou seja, todos os dados da página retornadas em texto (sem tags HTML ou qualquer tipo de sujeira)

### :bookmark_tabs: **Execução**
O arquivo pode ser executado facilmente com "python3 crawler.py [QUERY]"

### :hammer: **Bibliotecas utilizadas**
- requests: biblioteca para execução de requisiçes (HTTP), integrando programas .py em web services
- BeautifulSoup: biblioteca para coleta e tratamento de dados da web.
- click: biblioteca para tratamento e contrução da interface CLI.



