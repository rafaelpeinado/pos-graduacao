# Engenharia de Dados I

* **Por que estudar Engenharia de Dados?**
  * O engenheiro de dados é o que vai criar o pipeline, o fluxo de dados que vai de um lugar para outro. Vai garantir que os dados sairão de um lugar para outro.
  * Por exemplo, um dev está fazendo um software para o departamento Y e precisa de dados que vem do departamento X, como fazemos isso? Em grandes empresas, vamos falar com o Engenheiro de Dados. O Engenheiro de Dados vai fazer o trabalho de arquitetar o fluxo de dados que vai permitir alimentar a aplicação com dados que precisamos com consistência, atualizados e críveis.
* **Engenharia de Dados x Ciência de Dados**
* **O que é Engenharia de Dados?**


## ETL

* Extract -> Transform -> Load
  * é o trabalho do engenheiro de dados


## Requisitos em grandes empresas

* Um profissional de ciência de dados deve:
  * Conhecer sobre estrutura de banco de dados
  * Saber como funciona um processo de ETL
  * Entender sobre modelagem de banco de dados
  * Compreender como funciona o uso de dados em produção
  * **Saber SQL**


## Nosso objetivo

* Introdução à estrutura de dados.
* Banco de dados relacional.
* SQL.
* Modelo ERD – construção e interpretação.
* O modelo e a álgebra relacional.


## Dados

* Dados x Informação.
* O que é um banco de dados?
  * É uma coleção de dados, que descreve, tipicamente, as atividades e relacionamentos de uma ou mais organizações.

**Exemplo:** MBA USP.


## SGBD

Sistema Gerenciador de Banco de Dados:
  * Software desenhado para auxiliar na manutenção, organização e coleta dos dados existentes em um banco de dados.

**Exemplo:** MySQL.


## Estruturas de Dados

Os dados que podemos utilizar dividem-se em:
* **Dados Estruturados:** são os dados que detêm formatos bem definidos, como os extraídos de planilhas ou bancos de dados relacionais no formato SQL.
* **Dados Semiestruturados:** Semelhantes aos dados estruturados, mas não obedientes na totalidade quanto à forma. Nesta linha estão os registros de linguagens baseadas em HTML e XML.
* **Dados Não Estruturados ou NoSQL:** não possuem um formato específico, são os dados coletados na sua forma original, como um texto, um vídeo, um fragmento de e-mail, um log de sistema ou ainda uma mera foto.


## Dados Estruturados

|  CPF  |  Nome  | Nota  |
| :---: | :----: | :---: |
|   x   |  José  |  10   |
|   y   | Maria  |   2   |
|   h   | Sílvio |   5   |


## Dados Semiestruturados

[
    {
        "CPF": "x",
        "NOME": "José",
        "NOTA": "10",
        "TELEFONE": "não consta"
    },
    {
        "CPF": "y",
        "NOME": "Maria",
        "NOTA": "2"
    },
    {
        "CPF": "h",
        "NOME": "Sílvio",
        "NOTA": "5",
        "RENDA": "Muito alta"
    }
]


## Dados Não Estruturados
* Imagens, vídeos, áudio, tweets, etc


## SGBD Relacional

Nosso foco será em SGBD relacional.

**Vantagens no uso de um SGDB:**
* Independência.
* Eficiência.
* Integridade e segurança.
* Administração simplificada dos dados.
* Controle de acesso.


## Modelo de dados

* Dados "guardados" no banco de dados conforme modelo. O SGDB nos permitirá olhar este modelo e fazer consultas conforme lógica pré-estabelecida.
* A descrição dos dados em termos de modelos é o que chamamos de **esquema (SCHEMA)**. Conforme exemplo abaixo:
  * Estudantes(CPF: string, Nome: string, Nota: Integer)


## Tipos de dados

* Os tipos de dados são classificados em diferentes categorias e permitem N formatos. Aqui iremos apresentar somente os mais comuns.
  * **Integer ou inteiro:** Exemplo: 1, 2, etc.
  * **Float:** Exemplo: 0.10, 10.25, etc.
  * **String:** Exemplo: “bom dia”, “meu nome é”, etc.
  * **Date:** Exemplo: 2021-01-01.
  * **Caso do VARCHAR e CHAR:**
    * CHAR para pouco caracteres
    * VARCHAR para muitos caracteres


## Modelo de dados

* Estudantes(CPF: string, Nome: string, Nota: Integer):
  * Isso nos diz que trata-se de uma tabela com três campos.
  * Modelo relacional implica que cada registro é único.
  * Restrições de integridade!


### Níveis de Abstração

#### Modelo conceitual

* Mais alto nível.
* Mais próximo da realidade do negócio.
* Descreve os relacionamentos entre as entidades presentes em um banco de dados.


##### Definições ERD

* **Entidade:** Algo que pode ser definido e que pode ter dados armazenados sobre ele — como uma pessoa, um objeto, conceito ou evento. Pense em entidades como substantivos. Exemplos: um cliente, estudante, carro ou produto.
* **Relacionamento:** Como entidades atuam umas sobre as outras ou estão associadas uma com a outra. Pense em relacionamentos como verbos. Por exemplo, o estudante pode se inscrever em um curso. As duas entidades seriam o aluno e o curso, e o relacionamento descrito é o ato de matricular-se, assim conectando as duas entidades.
* **Atributo:** A propriedade ou característica de uma entidade, muitas vezes representada por um oval ou círculo.


#### Modelo Lógico

* Como efetivamente os dados estarão dispostos em tabelas no banco de dados.
* Leva em conta limitações do banco e SGBD.
* Define chaves primárias, estrangeiras e restrições de integridade.


#### Modelo Físico

* Implementação própria dita. Como inserir os dados e criar tabelas e todo o esquema.
* Mais baixo nível.
* Como serão armazenados os dados.
* Métodos de restauração, backup.


## Query

Dada a existência de um banco de dados, podemos perguntar:
* Quantos estudantes estão matriculados em um curso?
* Quantos cursos estão ativos?
* Qual a idade média dos estudantes?
* Qual a idade média dos estudantes de um determinado curso?
**Entra SQL**


## SQL

* **DML – data manipulation language.**
* Universalmente aceita.
* Própria para usar álgebra relacional.


## Introdução ao SQL

### SQL

* **Structured Query Language:**
  * Origem – IBM.
  * Não precisamos da forma como chegar no resultado – definimos o resultado.
  * Linguagem declarativa.


### Aspectos Importantes

* **DML – manipulação de dados.**
* **DDL – definição de dados.**
* Acesso remoto a bases de dados.
* Gerenciamento de transações.
* Segurança.


### Forma básica de uma query

```sql
SELECT [DISTINCT] lista-seleção
FROM lista-origem
WHERE qualificação
```


### Componentes

* **lista-seleção** – colunas que devem aparecer no resultado.
* **lista-origem** – quais as tabelas que serão consultadas.
* **Qualificação** – condições a serem impostas na consulta.


### Observações

* Nome do campo tem que ser exato.
* SQL é case insensitive.
* Separe o nome das colunas por vírgulas.


### Lista-origem e Alias

* Alias é o “apelido”. Muito usado em SQL.
* Você pode utilizá-lo para facilitar o entendimento de sua query.


### Qualificação

* A qualificação são as famosas cláusulas **where**.
* Essas são uma combinação de expressões booleanas de condições na forma de expressões.
* Em termos de álgebra, são definições de subconjuntos.


## Introdução ao ETL

* Extract, Transformation and Load.
* A integração de dados ETL é um processo de três etapas em que os dados são extraídos de uma ou mais fontes de dados, convertidos para o estado necessário e carregados em um banco de dados ou data warehouse em nuvem.


### Frameworks para ETL
* Apache Airflow
* python
* Informatica
* pentaho


## Observações e Referências
* [IEEE](https://www.ieee.org/)









