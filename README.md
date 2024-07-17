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



# Engenharia de Dados II
## Introdução

### Perguntas
* Como unir as informações das tabelas?
* Como obter informações de curso a partir de estudantes?
* Como realizar consultas bem performáticas com qualificações inseridas?
* Como garantir que o modelo seja robusto a transações.


## Transações
* Execução no banco de dados.
* Garante integridade – exemplo de compra de lugares no teatro.
* Sensação de execução local com isolamento e proteção contra perdas.
* Conceito de lock.


### Locking Protocol
* Regras que garantem que, mesmo que várias pessoas executem queries ao mesmo tempo, o resultado líquido será o mesmo que teria ocorrido se as mesmas tivessem sido executadas em fila.
* o lock irá garantir que o objeto consultado não possa ser acessado por meio de outras transações
* Exclusive Lock e Shared Lock.


## Relacionamento
* Como garantir robustez ao modelo do negócio? Além da robustez de transações -> restrições.
* O relacionamento entre entidades. Como se relacionam estudantes e cursos?
* A tabela deve ter consistência interna e os relacionamentos dela com as demais também.


## Restrições de Integridade
* Restrições de chave, de relacionamento e gerais.
* Restrições de chave: um subconjunto mínimo de campos de uma relação que identifica tupla única.
* Ou seja, campo(s) definidos como chave devem garantir que a linha selecionada seja única.


### Exemplo
| CPF | Nome  | Curso            |
| --- | ----- | ---------------- |
| xxx | João  | Ciência de Dados |
| yyy | João  | Medicina         |
| hhh | Pedro | Medicina         |

| Nome  | Sobrenome | Curso            |
| ----- | --------- | ---------------- |
| João  | Silva     | Ciência de Dados |
| João  | Marinho   | Ciência de Dados |
| Pedro | Guedes    | Ciência de Dados |


## Chave Primária
* Uma determinada tabela pode ter várias chaves = chaves candidatas
* Chave primária é definida pelo DBA de forma que o SGBD faça as averiguações por meio da mesma.
* Chave primária bem definida é importante pois suscita a criação de índices o que torna as consultas mais performáticas.


## Formas Normais
* Série de regras que garantem se um BD foi bem projetado
* Mostra a importância de uma chave primária bem definida
* Objetivo:
1. Garantir informação sem redundância
2. Garantir eficiência na obtenção dos dados


### 1ª forma normal
* Cada linha é uma informação. Não podem existir grupos repetidos ou atributos com mais de um valor.
* **PESSOAS**: `{ID, NOME, ENDERECO, TELEFONES}`

* **PESSOAS**: `{ID, NOME, ENDERECO}`
* **TELEFONES**: `{PESSOA_ID, TELEFONE}`


### 2ª forma normal
* Todas as colunas que não participam da chave primária são dependentes de todas as colunas que compõem a chave primária.
* **ALUNOS_CURSOS**: `{ID_ALUNO, ID_CURSO, NOTA, DESCRICAO_CURSO}`

* **ALUNOS_CURSOS**: `{ID_ALUNO, ID_CURSO, NOTA}`
* **CURSOS**: `{ID_CURSO, DESCRICAO}`


## Restrições Gerais
* Restrições de negócio, principalmente.
* Exemplo: inserção de idade.
* Os modernos SGBD já têm ferramentas que permitem criar tais restrições.


## Como lidar com modelos com mais de uma tabela?
### Chave Estrangeiras
* Chave primária de outra tabela
* Essa chave nos permite ligar tabelas diferentes de forma a garantir a unicidade da relação.
* O nome da chave estrangeira não precisa ser o mesmo da chave primária = o que importa é o conteúdo!


### ACID
* Atomicity, Consistency, Isolation, Durability
* Conjunto de propriedades em transações de bancos de dados que são importantes para garantir a validade dos dados mesmo que ocorram erros durante o armazenamento ou problemas mais graves no sistema, como crashes ou problemas físicos em um servidor. As propriedades ACID são fundamentais para o processamento de transações em banco de dados.

* **Atomicidade:** garante que cada transação seja tratada como uma entidade única, a qual deve ser executada por completo ou falhar completamente
* **Consistência:** os dados que são gravados devem sempre ser válidos
* **Isolamento:** permite deixar o banco de dados no mesmo estado em que ele estaria caso as transações fossem executadas em sequência
* **Durabilidade:** a propriedade da durabilidade garante que uma transação, uma vez executada (efetivada), permanecerá neste estado mesmo que haja um problema grave no sistema


### Cardinalidade
* **Cardinalidade:** indica quantas ocorrências de uma Entidade participam no mínimo e no máximo do relacionamento.

**Tipos de relacionamento:**
* Um para um
* Muitos para um
* Muitos para muitos


* Cardinalidade mínima: define se a relação é obrigatória
* Cardinalidade máxima: define a quantidade máxima de ocorrências da Entidade que pode participar do Relacionamento


## Operando com SQL
### JOIN, LEFT JOIN, RIGHT JOIN, INNER JOIN
* Especifica como será feita a junção entre duas tabelas. 


### UNION ALL vs. UNION
* Tabelas de mesma estrutura que serão “empilhadas”.
* UNION ALL inclui duplicatas, UNION aplica um DISTINCT.


## Nested Queries
* Resultado de uma query anterior pode ser utilizada na atual.
* Exemplo de uso com `IN`.


## ODBC e JDBC
* Java Database Connectivity – SUM
* Open Database Connectivity – Microsoft
* Permite a execução de SQL dentro do banco a partir de aplicações.


## Queries

Ambos tem o mesmo resultado:

```sql
SELECT * FROM payment A
LEFT JOIN customer B
ON A.customer_id = B.customer_id;

SELECT * FROM payment A
LEFT JOIN ( SELECT * FROM customer ) B
ON A.customer_id = B.customer_id;
```


## Observações e Referências
* [IEEE](https://www.ieee.org/)



