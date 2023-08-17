# Palestra: Os desafios da arquitetura de software - Guilherme Bezerra de Lima
Antes de escolher uma linguagem, nós precisamos saber como vamos escalar essa aplicação, quais desafios vamos encontrar.

Tim Berners-Lee, criador do www "Os dados são preciosos e durarão mais do que os próprios sistemas."

Não há decisões fáceis na arquitetura de software, pois quando falamos de arquitetura de software sempre existirá diversos desafios. Entenda porque. Qual a relevancia para:
* Desempenho
* Elasticidade
* Escalabilidade
* Otimizar características operacionais
* Contratos
* Decisões

Temos diversos lugares para aprender Linguages de programação, Frameworks e Padrões/Padrões de Projetos. Por exemplo, Livro, Blog, YouTube, Stack Overflow etc

Por que existem tão poucos livros sobre arquitetura em comparação com tópicos técnicos como frameworks, linguagens, e assim por diante?
  * Porque os arquitetos raramente enfrentam problemas comuns.

Não podemos buscar o **melhor design** em arquitetura de software. Temos que buscar **a melhor combinação** de vantagens e desvantagens.

**Nenhuma** característica de arquitetura se sobressai sozinha, mas o **equilíbrio** de todas as caracterísicas concorrentes promovem o sucesso do projeto.
Isto é, não é apenas uma característica do software que o definirá como bom ou ruim, mas um conjunto deles gerando uma experiência positiva.

**Exemplos de arquiteturas**
* **Fortnite**
  * 31,3 milhões de jogadores ativos
    * Evento entre Fortnite e o rapper Travis Scott no Metaverso teve a participação de 27,7 milhões de jogadores únicos - sendo o pico de 12 milhões de usuários simultâneos.
  * Infra e Ops do Fortnite: utiliza a AWS como principal fonte de distribuição das aplicações.
    * A cada mês, a Epic lida com aproximadamente com dois petabytes de dados
    * Fortnite é executado em servidores em 24 das 27 zonas de disponibilidade da AWS
      * Fortnite usa a elasticidade da AWS para fornecer mais capacidade quando os usuários aumentam.

Então é só copiar a infra do Fortnite? Claro que não!!! Pois muitos problemas apresentam desafios únicos porque combinam o ambiente e as circunstâncias exatas de uma organização.

Outro desafio da arquitetura de software
**Acoplamento**
* Duas partes de um sistema de software são **acopladas** se a **mudança** em uma parte puder causar uma **mudança** na outra.
* **Tipos de acoplamentos**
  * **Acoplamento estático:** dependências operacionais
  * **Acoplamento dinâmico:** dependências de comunicação
* **Definindo o tamanho de acoplamento:**
  * **serviços pequenos:** problemas transacionais e de orquestração
  * **serviços grandes:** problemas de escala e distribuição

**Exemplo Nubank**
* **Microserviço** desde o primeiro dia
* Possuem mais de 40 milhões de clientes em diferentes países da América Latina

* **Infra e Ops da Nubank**
  * **Infraestrutura imutável:** conectada à ideias de programção funcional, cujo a ideia central é o conceito de imutabilidade
    * Banco de dados [Datomic](https://www.datomic.com/): a cada mudança teremos um histórico e será salvo
  * **Comunicação de serviço e mensagens assíncronas:** o serviço inicial publicará de forma confiável uma mensagem para ser posteriormente consumida pelo próximo serviço no fluxo.

**Exemplo StackOverflow**
* 4 biilhões de requisições por mês
* Arquitetura monolítica: 3000 res/s e 800 milhões de consultas SQL por dia

* **Infra e Ops do Stack Overflow**
* Servidores on premises (obs: utilizam nuvem, porém eles usam em um servidor próprio na qual eles têm controle)
* Monolítica
* Banco de dados relacional


**A arquitetura de software é por natureza abstrata**
Por exemplo, o StackOverflow que lida muito mais com texto consegue ser um monolito e funcionar muito bem. Por outro lado, a Nubank que é um grande banco não conseguiria rodar em uma aplicação só. Ou seja, os contextos são completamente diferentes.

Sendo assim:
* Tome decisões
* Cumpra das decisões
* Analise continuamente a arquitetura
* Manter-se atualizado sobre arquitetura
* Conheça o negócio e suas regras (a aplicação precisa de uma resposta o mais rápido possível, por exemplo)
* Desenvolver habilidades interpessoais, pois

**ARQUITETURA DE SOFTWARE SE TRATA MAIS DE PESSOAS, DO QUE CÓDIGO.** Ou seja, se for um monolito, por exemplo, a equipe precisa trabalhar mais junto. Já se for um microserviço pode ter grupos menores. Além disso, a aplicação tem que ser uma boa experiência para o usuário.


