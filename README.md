# NoSQL x SQL I
## O que é um banco de dados?
- **Definição de Banco de Dados:** um banco de dados é uma coleção estruturada de informações que facilita o acesso e a manipulação de dados
- **Acesso e Recuperação:** os bancos de dados permitem que os usuários acessem e recuperem dados de maneira rápida e eficiente, otimizando processos
- **Sistemas gerenciadores de bancos de dados (SGBDs):** são softwares que permite a criação, manipulação e administração de bancos de dados


## Tipos de bancos de dados
- Transacionais (OLTP) (Online Transaction Processing)
- Analíticos (OLAP) (Online Analytical Processing)

- Relacional SQL
- NoSQL (Not Only SQL)
- New SQL (Hybrid)


## ACID: Atomicidade, Consistência, Isolamento e Durabilidade
- **Atomicidade:** atomicidade assegura que todas as partes de uma transação sejam concluídas com sucesso ou nenhum delas é aplicada
- **Consistência:** consistência mantém a integridade dos dados durante e após as transações, garantindo que os dados estejam sempre corretos
- **Isolamento:** isolamento garante que as transações ocorram independentemente, evitando conflitos e interferências entre elas.
- **Durabilidade:** durabilidade assegura que os resultados de uma transação sejam permanentes, mesmo em caso de falhas no sistema


## Arquiteturas Modernas de Bancos de Dados
- **On Premises:** servidores locais
- **IaaS:** instalado manualmente ou por templates
- **PaaS - Capacidade gerenciada:** Múltiplas ofertas - Conceito de **Instância**
- **PaaS Serverless:** Múltiplas ofertas, até SaaS


## Arquitetura e Escalabilidade de Bancos de dados
### Transações e Controle de Concorrência
- **Transações** garantem a integridade dos dados em operações complexas
- **Commit** é o processo de conclusão de uma transação
- **Rollback** é o processo de cancelamento de uma transação
- **Locks** são utilizados para evitar acessos simultâneos a dados críticos
- **Deadlocks** ocorrem quando duas transações bloqueiam recursos mutuamente
- Otimização envolve técnicas para minimizar locks e deadlocks


### Escalabilidade de Bancos de Dados
- Escalabilidade **vertical** adiciona recursos a um único servidor para aumentar a capacidade
- Escalabilidade **horizontal** envolve adicionar mais servidores para distribuir carga, no que chamamos de **clusters**
- Estes **clusters** são baseados em múltiplos servidores (nós) conectados que podem servir para balanceamento de carga e/ou alta disponibilidade do banco de dados


### Clusters
- **Clusters** garantem alta disponibilidade e **failover** automático em banco de dados
- Clusters são compostos de **nós**, que são múltiplas máquinas (servidores) interconectados
- A **replicação de dados** é essencial para manter a integridade e a consistência entre os nós
- Ambientes **híbridos** (Cloud x On Premises ou MultiCloud) combinam soluções em nuvem e locais para flexibilidade
- Estratégias de **Load Balancing** melhoram o desempenho em clusters
- O monitoramento contínuo é crucial para a manutenção e operação eficaz dos clusters


## Fundamentos do Modelo Relacional e SQL
### Modelo Relacional
- **Esquema:** os bancos de dados SQL/Relacionais, precisam ter um **esquema pré-definido**, antes de serem utilizados
- **Estrutura de Tabelas:** o modelo relacional organiza dados em **tabelas**, facilitando a representação de **entidades** e seus **atributos**
- **Chaves Primárias e Estrangeiras:** as chaves primárias, ou Primary Key (PK) identificam **registros únicos**, enquanto as chaves estrangeiras criam relações entre tabelas, promovendo a integridade dos dados. Já uma chave estrangeira, ou Foreign Key (FK), é uma referência a uma chave primária ede outra tabela relacional.
- **Facilidade de Busca:** o modelo relacional permite **buscas eficientes** e conexões entre diferentes conjuntos de dados, melhorando a análise de informações


### Integridade Referencial e Normalização
- **Integridade referencial** garante a **consistência** dos dados entre tabelas
- **Chaves primárias** e **estrangeiras** são fundamentais para a integridade Referencial
- **Normalização** organiza dados para reduzir redundâncias e dependências indesejadas.


### O que é SQL?
- SQL (**Structured Query Language**) é uma linguagem de programação usada para gerenciar e manipular bancos de dados
- **Qual o papel da linguagem SQL na estruturação de dados?** - a linguagem SQL desempenha um papel essencial na estruturação de dados, pois fornece comandos específicos para organização, armazenamento, recuperação e manipulação de informações


![Estrutura SQL](./assets/estrutura-sql.png)



## Introdução ao NoSQL
### O que é NoSQL?
- **Definição de NoSQL:** **NoSQL** refere-se a uma categoria de bancos de dados que não utilizam o modelo relacional, focando em flexibilidade e escalabilidade. Não possui **esquema** pré-definido
- **Alta Velocidade e Escalabilidade:** os bancos de dados NoSQL são projetados para gerenciar grandes volumes de dados com **alta velocidade** de leitura e gravação, permitindo operações em **tempo real**
- **Flexibilidade na Estrutura de Dados:** uma das principais vantagens dos bancos de dados NoSQL é a **flexibilidade** na estrutura de dados, permitindo armazenar informações não estruturadas e semiestruturadas


### CAP Theorem
- **Definição do Teorema CAP:** o Teorema CAP explica a relação entre consistências, disponibilidade e tolerância à partição em sistemas de banco de dados distribuídos
- **Consistência e Disponibilidade:** ao projetar um sistema NoSQL, você pode priorizar consistência e disponibilidade, mas isso pode comprometer a tolerância à partição
- **Impacto no Desempenho:** a escolha de quais propriedades priorizar impacta diretamente o desempenho e a integridade dos dados em um sistema distribuído


### Tipos de bancos NoSQL
- **Bancos de Dados Chave-Valor:** os bancos de dados chave-valor armazenam dados como pares de chave e valor, ideais para acesso rápido e escalável
- **Banco de Dados de Documentos:** bancos de dados de documentos armazenam dados em documentos flexíveis, geralmente em formato JSON, facilitando a gestão de dados semiestruturados
- **Banco de Dados Colunares:** os bancos de dados colunares armazenam dados em colunas em vez de linhas, otimizando consultas de grandes volumes de dados
- **Banco de Dados de Grafos:** bancos de dados de grafos são projetados para representar e consultar relacionamentos complexos entre dados de forma eficiente


### Escalabilidade em NoSQL
- **Escalabilidade Horizontal e Vertical:** os bancos de dados NoSQL permitem escalabilidade horizontal, facilitando a adição de novas máquinas ao cluster, bem como vertical aumentando a capacidade em um único servidor/instância
- **Desempenho em Aumento de Dados:** NoSQL é projetado para lidar com grandes volumes de dados sem comprometer o desempenho, mesmo com tráfego crescente


### Exemplos de Bancos de Dados Transacionais NoSQL - Não Relacionais
- **Modelo documento:** MongoDB, CouchDB
- **Modelo colunas:** Cassandra, Hbase, Bigtable
- **Modelo grafos:** Neo4j, Gremlin, ArangoDB
- **Modelo chave-valor:** Redis Cache, DynamoDB


### Exemplos Banco de Dados Analíticos NoSQL - Não Relacionais
- Azure Synapse Analytics
- Microsoft Fabric
- databricks
- Cloudera
- elastichsearch














