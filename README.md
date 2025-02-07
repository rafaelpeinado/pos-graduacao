# Domain Driven Design I
- Construir software está **mais desafiador** do que nunca.

- **Alguns motivos:**
  - **Complexidade dos negócios:** o sistema de software precisa atender demandas específicas
  - **Sistemas perfeitos:** o mercado exige interfaces impecáveis, alta performance e disponibilidade 24/7
  - **Diversidade tecnológica:** a variedade de linguagens, frameworks, e ferramentas disponíveis torna a escolha das tecnologias certas um desafio
- **Inteligência Artificial**

- **Tendências tecnológicas em constante mudança**

- **Um serviço online de streaming**
 | Empresa       |           Tecnologias           |       Clientes       |
 | :------------ | :-----------------------------: | :------------------: |
 | Netflix       |  AWS, Kubernetes, Java, Python  |     247 milhões      |
 | Amazon Prime  |     AWS, Java, React Python     |     200 milhões      |
 | Disney+       | AWS, Node.js, React, JavaScript |     146 milhões      |
 | Nossa Empresa |        AWS, Java, Python        | Milhões de clientes? |


## DDD
- Criar sistemas que **reflitam de forma precisa** as **regras**, **processos** e **linguagens específicas** do **domínio** em que o software será aplicado.

#### Domínio do software
- Todo programa de software se relaciona com alguma atividade ou interesse de seu usuário 
  - Intangíveis
  - Físico

- **Software valioso** está alinhado com uma **equipe de engenharia que _conhece_** sobre a **atividade do negócio**

- **Código claro** sempre parece ter sido escrito por alguém que se **importa**.
- O DDD prioriza a **colaboração** entre **desenvolvedores** e **especialistas** no domínio
- Um **domínio** de negócios define a **principal área** de atividade de uma empresa.
- **Serviço** que a empresa **fornece** aos seus clientes


#### Subdomínios
- **Netflix:**
  - **Domínio principal:** entretenimento digital por streaming
  - **Subdomínios:** Catálogo de Conteúdo; Indexação; Gestão dos Direitos; Infraestrutura; Algoritmo de Recomendações; **Monetização e Assinatura**;


#### Especialistas de domínio
- Os especialistas de domínio **não são** os **analistas** que reúnem os requisitos nem os **engenheiros** que projetam o sistema.


#### Linguagem Ubíqua
- Comunicação
- **Um dos pilares do DDD:** é um vocabulário compartilhado entre desenvolvedores e especialistas no domínio
- **Elimina ambiguidades:** desenvolvedores, analistas de negócios e stakeholders, usem os mesmos termos com os mesmos significados
- **Melhora comunicação:** reduz mal-entendidos e garante que todos compreendam e trabalhem de acordo com os mesmos conceitos do domínio

- **Problema:** no sistema, há uma função chamada **Disponibilidade de Produto**, mas o termo não é bem definido entre a equipe

##### Disponibilidade de Produto
- **Equipe de negócios:** produtos que podem ser vendidos, considerando vendas realizadas e em processo de compra
- **Equipe de desenvolvimento:** concentra-se na quantidade física de produtos em estoque que podem ser vendidos
- **Especialista do Domínio:** entendo como a **capacidade de um item ser adquirido**, levando em conta tanto o **estoque real quanto a reserva de itens no carrinho de compras**

- **6 ações** práticas para implementar uma **linguagem ubíqua**
  - Documentos
  - Reuniões Regulares
  - Nomes significativos no Código
  - Alinhamento
  - Wiki interno
  - Revisar e Refatorar


###### Exemplo
- Carrinho de compras
- [Abandono de carrinho de compras](https://rockcontent.com/br/blog/abandono-de-carrinho/)


## Estudo de Caso
- **Sistema** de gestão de **Cursos**


### Entidades
- Objetos identificados exclusivamente por uma **identidade**, independentemente de seus atributos
  
#### Identificação de Conceitos de Domínio
- **Entidades:**
  - Alunos
  - Curso
- **Objetos de Valor:**
  - Telefone do Aluno
  - Código de um curso
- **Eventos do Domínio:**
  - Aluno Cadastrado
  - Matrícula Realizada
  - Curso Concluído

- **Objetos de valor:** são definidos por seus **atributos** e **não possuem** identidade própria.
- **Eventos do Domínio:** **mudanças** ou situações significativas no negócio, com uma natureza imutável (representam algo que aconteceu).



# Domain Driven Design II
## Implementando Domain-Driven Designer
- **DDD** não se trata exclusivamente de **tecnologia**


## Aplicativo centrado em Dados?
- CRUD (Create, Read, Update, Delete)


## Sistema de Gestão de Cursos
- A classe **matrícula** desempenha um papel fundamental aqui


## Tática vs Estratégico
- Tática é mais prático: trabalha nas camadas e em como as classes serão chamadas, por exemplo
- Estratégico é mais amplo 

- Bounded **Context**: é um limite claro de onde o modelo é definido e vai ser usado


### Aluno
- **id:** deve ser um número inteiro maior que zero
- **nome:** deve ser uma string não vazia. O código atual não impõe essa restrição explicitamente, mas é uma regra de negócio implícita
- **email:** deve ser um endereço de email válido
- **telefone:** deve seguir o formato "DDD-99999-9999"


### Treinamento
- **id:** deve ser um número inteiro maior que zero
- **codigo:** deve ser o formato "XX99", onde XX são duas letras maiúsculas e 99 são dois números
- **descricao:** deve ser uma string com informações sobre o treinamento
- **carga_horaria:** deve ser um número inteiro maior que zero
- **capacidade:** deve ser um número inteiro maior que zero


### Caso de uso
Atendente -> Matricular um aluno em um treinamento específico


### Matrícula
- Um aluno só pode ter **uma matrícula ativa por vez**
  - Um aluno não pode se matricular em um novo treinamento se já estiver matriculado em outro com status "Ativo".
- Um treinamento tem um **limite de alunos**
  - Um aluno só pode se matricular em um treinamento se houver vagas disponíveis
- Um treinamento possui um **código único**
  - Não podem existir dois treinamentos com o mesmo código
- **Aluno e Treinamento devem existir:**
  - Para criar uma matrícula, o aluno e o treinamento indicados devem existir previamente no sistema


### Fluxo Principal
- O Atendente solicita a matrícula de um aluno em um treinamento
- O sistema valida os dados de entrada
- Se todas as validações passarem, o sistema cria uma nova matrícula com o status "Ativo".
- Matrícula é concluída


## Camada Anticorrupção (Anti-Corruption Layer - ACL)
- O principal objetivo é proteger o domínio de ser corrompido de aplicações externas, como por exemplo, código de treinamento



