# API DADOS PÚBLICOS

Neste arquivo estão as instruções necessárias para a utilização das bases de dados de vacinação contra a Covid-19, segurança pública e desenvolvimento social no Estado do Ceará no ano de 2021.

## Banco de Dados
#### Dependências
[PostgreSQL, preferencialmente na versão 10](https://www.postgresql.org/ "PostgreSQL, preferencialmente na versão 10")

Para a importação do banco de dados, será utilizado o arquivo TCC-2022_07_06_10_49_02-dump.sql disponível na pasta raiz deste repositório.
1. Crie um banco de dados.
`create database dados`
2. Import os dados através do terminal.
`psql dados < TCC-2022_07_06_10_49_02-dump.sql`

Uma vez importados os arquivos no banco, os dados estão prontos para uso, consulta e processamento.

## Criação da API 

#### Dependências

[Docker](https://docs.docker.com/get-docker/ "Docker")
[Docker compose](https://docs.docker.com/compose/install/ "Docker compose")

Uma vez instaladas as dependencias, vá até o diretório /graphql-engine/stable/install-manifests/docker-compose e execute o seguinte comando:
`docker-compose up -d`

Verifique, após o término das instalações, através do comando `docker ps` se o processo da graphql-engine está em execução, tal qual na imagem abaixo:

![image](https://user-images.githubusercontent.com/42448044/177585018-36053c5d-8cd5-4c26-8017-3b83e4b1cf4f.png)


Acesse o browser através do localhost na porta em que o processo está sendo executado.

1. Vá até o Menu de Data e Conecte-se ao banco de dados utilizando a string de conexão do seu banco. Importante: Substitua localhost por host.docker.internal, para que o seu banco fique acessível para o conteiner da aplicação.
![image](https://user-images.githubusercontent.com/42448044/177586239-a5957e38-46b0-4af0-91bb-90631f0ab9f4.png)


2. Após a conexão, selecione o banco a se trabalhar, e clique em Track em todas as tabelas e constraints do banco.

Vá até as configurações e selecione Import Metadata:
![image](https://user-images.githubusercontent.com/42448044/177585949-ee478461-ac28-40d5-9036-ad288de0aab5.png)

Importe o arquivo hasura_metadata_2022_07_04_05_49_45_860.json

Todos os dados de consultas, requisições e demais configurações serão importadas. 

Agora, todos os endpoints estão disponíveis e podem ser consumidos através de métodos Http.
![image](https://user-images.githubusercontent.com/42448044/177586392-d8317ce1-9766-4dbf-9533-2b1bb20c549e.png)

