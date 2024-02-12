# Microsserviços I
## Fundamentos
### Histórico
* **Mainframe Monolithic (1980s)**
  * Input / Output
  * Processing
  * Data Storage
  * Reporting
  * Time Division Multiplexing
* **Client-Server (1990s)**
  * GUI
  * Main Computing on Server
  * I/O at Client
  * LAN
* **Web Application (2000s)**
  * GUI - Browser
  * Main Computing on Web Server
  * Layered Components
  * Internet Based
* **Service Oriented Architecture (2010s)**
  * Layered Services
  * SOAP WebServices
  * Binary Communication 
  * Internet Based
* **Microservices (Present)**
  * Granular Services
  * REST / Message Queue
  * Based Upon Subdomains
  * Internet Based

**Histórico de Tecnologias**
* 1999: Continuous Integration via XP
* 2001: 
  * Feb: Agile Manifesto
* 2006: AWS EC2
* 2009:
  * DevOps
  * Java EE6
* 2010: NETFLIX to AWS
* 2011:
  * May: DropWizard
  * June: Vert.x
* 2012:
  * March
    * Ribbon
    * Hystrix
    * Microservices Assess - Thoughtworks Radar
  * July: 
    * Eureka
* 2013:
  * March: Docker
  * Sept: Spring Boot
* 2014:
  * March: Microservices Defined - Thoughtworks Fowler, Lewis
  * June: Kubernetes


### Pessoas e ideias
* Fred George - ThoughtWorks - Bayesian Principles - 2004
* Peter Rodgers - Micro-Web-Services - 2005
* Alistair Cockburn - Hexagonal Architecture - 2005
* James Lewis - ThoughtWorks - Microservices - 2011
* Martin Fowler - ThoughtWorks - Microservices - 2011

### O Termo Microsserviços
[Microservices: a definition of this new architectural term](https://martinfowler.com/articles/microservices.html)
"Microservices" - yet another new term on the crowded streets of software architecture. Although our natural inclination is to pass such things by with a contemptuous glance, this bit of terminology describes a style of software systems that we are finding more and more appealing. We've seen many projects use this style in the last few years, and results so far have been positive, so much so that for many of our colleagues this is becoming the default style for building enterprise applications. Sadly, however, there's not much information that outlines what the microservice style is and how to do it.

In short, the microservice architectural style [1] is an approach to developing a single application as a suite of small services, each running in its own process and communicating with lightweight mechanisms, often an HTTP resource API. These services are built around business capabilities and independently deployable by fully automated deployment machinery. There is a bare minimum of centralized management of these services, which may be written in different programming languages and use different data storage technologies.

[1] The term "microservice" was discussed at a workshop of software architects near Venice in May, 2011 to describe what the participants saw as a common architectural style that many of them had been recently exploring. In May 2012, the same group decided on "microservices" as the most appropriate name. James presented some of these ideas as a case study in March 2012 at 33rd Degree in Krakow in Microservices - Java, the Unix Way as did Fred George about the same time. Adrian Cockcroft at Netflix, describing this approach as "fine grained SOA" was pioneering the style at web scale as were many of the others mentioned in this article - Joe Walnes, Daniel Terhorst-North, Evan Botcher and Graham Tackley.


É um estilo arquitetural, ou seja, uma forma de trabalhar, criar e consolidar tecnologias que vai indicar uma direção


### Empresas e Ideias
* Amazon
* [AWS](https://queue.acm.org/detail.cfm?id=1142065)
* [ThoughtWorks](https://www.thoughtworks.com/insights/topic/microservices)
* [Netflix](https://netflixtechblog.com/redesigning-the-netflix-api-db5a7221fcff)
* [Google](https://cloudplatform.googleblog.com/2015/01/in-coming-weeks-we-will-be-publishing.html)


### Preparação para Microsserviços *
[Implementing Microservices on AWS](https://docs.aws.amazon.com/whitepapers/latest/microservices-on-aws/microservices-on-aws.html)
Arquiteturas de microsserviços combinam vários conceitos, tecnologias e padrões:
* Desenvolvimento de Software Ágil
* Arquiteturas Orientadas à Serviço: Service Oriented Architecture (SOA)
* API-first Design
* CI/CD
* Design Patterns Twelve-Factor App


### O que são Serviços Web?
Um **serviço web** é qualquer software disponibilizado pela Internet que usa um **formato padronizado**, como eXtensible Markup Language (XML) ou JavaScript Object Notation (JSON), para a solicitação e resposta de uma interação através de **Application Programming Interface (API)**.

Cliente --- mensagem de solicitação --> Internet --- mensagem de solicitação --> Serviço Web
        <---- mensagem de resposta ----          <---- mensagem de resposta ---- 


### O que significa API? *
* API significa Application Programming Interface (Interface de Programação de Aplicação). No contexto de APIs, a palavra Aplicação refere-se a qualquer software com uma função distinta.
* A interface pode ser pensada como um contrato de serviço entre duas aplicações. Esse contrato define como as duas se comunicam usando solicitações e respostas.
* A documentação de suas respectivas APIs contém informações sobre como os desenvolvedores devem estruturar essas solicitações e respostas.


### O que é uma API?
* APIs são mecanismos que permitem que dois componentes de software se comuniquem usando um conjunto de definições e protocolos.
* Por exemplo, o sistema de software do instituto meteorológico contém dados meteorológicos diários.
* A aplicação para previsão do tempo em seu telefone "fala" com esse sistema por meio de APIs e mostra atualizações meteorológicas diárias no telefone.


### Como as APIs funcionam?
* A arquitetura da API geralmente é explicada em termos de cliente e servidor.
* A aplicação que envia a solicitação é chamada de cliente e a aplicação que envia a resposta é chamada de servidor.
* As operações podem ser síncronas ou assíncronas.
* Então, no exemplo do clima, o banco de dados meteorológico do instituto é o servidor e o aplicativo móvel é o cliente.


### O que é API Web?
* Uma API Web ou API de serviço da Web é uma interface de processamento de aplicações entre um servidor da Web e um navegador da Web.
* A API REST é um tipo especial de API Web que usa o estilo de arquitetura padrão explicado acima.
* Os diferentes termos que abrangem as APIs, como API Java ou APIs de serviço, existem porque, historicamente, as APIs foram criadas antes da World Wide Web. As APIs Web modernas são APIs REST e os termos podem ser usados de forma intercambiável.

**Obs: A maioria dos serviços Web são APIs, mas nem todas as APIs são serviços Web**


### O que são integrações de API?
* As integrações de API são componentes de software que atualizam automaticamente os dados entre clientes e servidores.
* Alguns exemplos de integrações de API são quando os dados automáticos são sincronizados com a nuvem por meio da galeria de imagens do seu telefone ou a data e a hora são sincronizadas automaticamente no seu laptop quando você viaja para um local com outro fuso horário.


### Acessibilidade de APIs?
* **APIs privadas:** elas são internas a uma empresa e são usadas apenas para conectar sistemas e dados dentro da empresa.
* **APIs públicas:** estas são abertas ao público e podem ser usadas por qualquer pessoa. Pode ou não haver alguma autorização e custo associado a esses tipos de APIs.
* **APIs de parceiros:** estas são acessíveis apenas por desenvolvedores externos autorizados para auxiliar as parcerias entre empresas.
* **APIs compostas:** estas combinam duas ou mais APIs distintas para atender a requisitos ou comportamentos complexos do sistema.


### O que é um endpoint de API e por que ele é importante?
* Os endpoint da API são os pontos de contato finais no sistema de comunicação da API. Estes incluem URLs de servidores, serviços e outros locais digitais específicos de onde as informações são enviadas e recebidas entre sistemas. Os endpoints da API são fundamentais para as empresas por dois motivos principais:
  1. **Segurança:** Os endpoint da API tornam o sistema vulnerável a ataques. O monitoramento da API é crucial para impedir o uso indevido.
  2. **Performance:** Os endpoints da API, especialmente os de alto tráfego, podem causar gargalos e afetar a performance do sistema.


### Como criar uma API?
1. **Planejar a API:**
   * As especificações da API, como OpenAPI, fornecem o esquema para o design da sua API
   * É melhor pensar em diferentes casos de uso com antecedência e garantir que a API esteja de acordo com os padrões atuais de desenvolvimento de API.
2. **Criar a API:**
   * Os designers de API fazem a prototipagem APIs usando código boilerplate.
   * Depois que o protótipo é testado, os desenvolvedores podem personalizá-lo de acordo com as especificações internas.
3. **Testar a API:**
   * O teste de API é o mesmo que o teste de software e deve ser feito para evitar bugs e defeitos.
   * As ferramentas de teste de API podem ser usadas para testar a resistência da API contra ataques cibernéticos.
4. **Documentar a API:**
   * Embora as APIs sejam autoexplicativas, a documentação da API funciona como um guia para melhorar a usabilidade.
   * APIs bem documentadas que oferecem uma série de funções e casos de uso tendem a ser mais populares em uma arquitetura orientadas a serviços.
5. **Comercializar a API:**
   * Existem marketplaces de API para desenvolvedores comprarem e venderem outras APIs.
   * Catalogar sua API pode permitir que você ganhe dinheiro com ela.


### Exercício: API
* [US National Weather Service](https://www.weather.gov/)
* [API](https://api.weather.gov/)
* [Documentação](https://www.weather.gov/documentation/services-web-api)
* Exemplos de chamadas das APIs:
  * https://api.weather.gov/gridpoints/TOP/31,80/forecast
  * https://api.weather.gov/points/39.7456,-97.0892
  * https://api.weather.gov/alerts/active?area=NY


### Principais tipos de APIs *
* Principais tipos de APIs e seu funcionamento, dependendo de quando e por que elas foram criadas:
  * **APIs REST**
    * Essas são as APIs mais populares e flexíveis encontradas na Web atualmente.
    * O cliente envia solicitações ao servidor como dados.
    * O servidor usa essa entrada do cliente para iniciar funções internas e retorna os dados de saída ao cliente.
  * **APIs RPC**
    * Essas APIs são conhecidas como Remote Procedure Calls (Chamadas de Procedimento Remoto)
    * O cliente conclui uma função (ou um procedimento) no servidor e o servidor envia a saída de volta ao cliente.
  * **APIs SOAP**
    * Essas APIs usam o SOAP - Simple Object Access Protocol (Protocolo de Acesso a Objetos Simples).
    * Cliente e servidor trocam mensagens usando XML.
    * Esta é uma API menos flexível que era mais popular no passado.
  * **GraphQL**
    * GraphQL é uma especificação, uma linguagem de consulta de API e um conjunto de ferramentas. GraphQL opera em um único endpoint usando HTTP.
    * Ela prioriza fornecer aos clientes exatamente os dados que eles solicitam e nada mais.
    * Foi projetada para tornar as APIs rápidas, flexíveis e amigáveis ao desenvolvedor.
    * Como alternativa ao REST, o GraphQL oferece aos desenvolvedores de frontend a capacidade de consultar vários bancos de dados, microsserviços e APIs com um único endpoint de GraphQL.
**Obs.:** Websocket, entre outros

### Comparação entre os principais tipos de APIs *
#### REST
* **Fundamento:** API design pattern
* **Características:** 
  * Orientado a recursos
  * Baseado em dados
  * Flexível
* **Formato de Dados:** JSON/XML/YAML/HTML/plain text
* **Curva de Aprendizado:** Fácil
* **Comunidade:** Grande
* **Casos de Uso:**
  * Todos os tipos de apps web
  * Apps Cloud
  * Serviços de computação em nuvem


#### RPC
* **Fundamento:** API design pattern
* **Características:** 
  * Orientado a ação
  * Alto desempenho
* **Formato de Dados:** JSON/XML/Thrift/Protobuf/FlatBuffers
* **Curva de Aprendizado:** Fácil
* **Comunidade:** Grande
* **Casos de Uso:**
  * Sistemas de microsserviços complexos
  * Aplicações IoT


#### SOAP
* **Fundamento:** Protocolo para criação de APIs
* **Características:** 
  * Padronizado
  * Altamente seguro
  * Foco em aplicações corporativas
* **Formato de Dados:** XML
* **Curva de Aprendizado:** Desafiadora
* **Comunidade:** Pequena
* **Casos de Uso:**
  * Serviços financeiros
  * CRM
  * Gerenciamento de Identidade
  * Integração de sistemas legado


#### GraphQL
* **Fundamento:** Linguagem de consulta e runtime server-side para APIs
* **Características:** 
  * Endpoint único
  * Requisições fortemente típadas
  * Buscas enxutas
  * Auto-documentável
* **Formato de Dados:** JSON
* **Curva de Aprendizado:** Média
* **Comunidade:** Em crescimento
* **Casos de Uso:**
  * Apps móveis de alto desempenho
  * Sistemas complexos
  * Arquiteturas baseadas em microsserviços


### REST
* O modelo REST (REpresentational State Transfer) representa uma das possibilidades para a criação de web services, com utilização semântica dos métodos HTTP (GET, POST, PUT e DELETE)
* O criador do modelo REST foi [Roy Fielding](https://roy.gbiv.com/), um dos principais autores de especificação HTTP e cofundador do projeto Apache HTTP Server
* O termo REST foi apresentado pela primeira vez em 2000 na tese de doutorado de Roy Fielding [Architectural Styles and the Design of Network-based Software Architectures](https://ics.uci.edu/~fielding/pubs/dissertation/top.htm)
* Uma requisição HTTP é equivalente a uma chamada de um método (operação) em um objeto (recurso) residente no servidor.
* Principais características de uma requisição REST:
  * <img src="https://d1.awsstatic.com/whatisimg/New-API-GW-Diagram.c9fc9835d2a9aa00ef90d0ddc4c6402a2536de0d%20(1).67a41a2ef9823282fe672434ddd56dd22c13d5a5.png">


### O que são APIs REST?
* A principal característica da API REST é a ausência de estado. A ausência de estado significa que os servidores não salvam dados do cliente entre as solicitações.
  * **Por isso temos que ter técnicas de cache e de sessão**
* As solicitações do cliente ao servidor são semelhantes aos URLs que você digita no navegador para visitar um site. A resposta do servidor corresponde a dados simples, sem renderização gráfica típica de uma página da Web.


### Quais são so benefícios da APIs REST?
#### Integração
*  As APIs são usadas para integrar novas aplicações com sistemas de software existentes. Isso aumenta a velocidade de desenvolvimento porque cada funcionalidade não precisa ser escrita do zero.
*  Você pode usar APIs para aproveitar o código existente.

#### Inovação
* Setores inteiros podem mudar a chegada de uma nova aplicação. As empresas precisam responder rapidamente e oferecer suporte à rápida implantação de serviços inovadores.
* Elas podem fazer isso fazendo alterações no nível da API sem precisar reescrever todo o código.

#### Expansão
* As APIs apresentam uma oportunidade única para as empresas atenderem às necessidades de seus cliente em diferentes plataformas.
* Por exemplo, a API de mapas permite a integração de informações de mapas por meio de sites, Android, iOS etc.
* Qualquer empresa pode fornecer acesso semelhante ao seus respectivos bancos de dados internos usando APIs gratuitas ou pagas.

#### Facilidade de manutenção
* A API atua como um gateway entre dois sistemas
* CAda sistema é obrigado a fazer alterações internas para que a API não seja afetada
* Dessa forma, qualquer alteração futura de código feita por uma parte não afetará a outra parte.


### Como proteger uma API REST?
* Todas as APIs devem ser protegidas por meio de autenticação e monitoramento adequados. As duas principais maneiras de proteger APIs REST incluem:

#### Tokens de autenticação
**Eles são usados para autorizar os usuários a fazer a chamada de API.** Os tokens de autenticação verificam se os usuários são quem afirmam ser e têm direitos de acesso aquela chamada de API específica. Por exemplo, quando você faz login em seu servidor de e-mail, seu cliente de e-mail usa tokens de autenticação para acesso seguro.


#### Chaves de API
**As chaves de API verificam o programa ou a aplicação que faz a chamada de API.** Elas identificam a aplicação e garantem que ela tenha os direitos de acesso necessários para fazer a chamada de API específica. As chaves de API não são tão seguras quanto os tokens, mas permitem o monitoramento da API para coletar dados sobre o uso. Você pode ter notado uma longa sequência de caracteres e números no URL do seu navegador ao visitar diferentes sites. Essa string é uma chave API que o site usa para fazer chamadas de API internas.


### APIs REST vs. RESTful
* Uma API RESTful segue ou implementa todas as exigências e restrições do estilo de arquitetura definido pelo criado do modelo REST (Roy Fielding) no processo de construção de uma aplicação.
* **As exigências para um API ser RESTful são:**
  1. Arquitetura cliente-servidor
  2. Comunicação stateless
  3. Cache
  4. Interface uniforme
  5. Sistema de camadas


### Exercício
#### cUrl
* cUrl é uma ferramenta de linha de comando utilizada para obter ou enviar dados, incluindo arquivos, usando a sintaxe URL
* Disponível para Sistemas Operacionais em UNIX/LINUX, Windows, MacOS
* Mais informações: [https://curl.se/](https://curl.se/)

##### Instalação cUrl
* GNU/Linux, distribuições em Debian (como o Ubuntu), execute: sudo apt install curl
* Windows: pré-instalado, mas caso não estiver, acesse: [https://curl.se/windows/](https://curl.se/windows/)
* Distribuições baseados em Arch Linux, execute: sudo pacman -S curl
* MacOS: pré-instalado, mas caso naõ estiver, execute: brew install curl (necessita instalar Brew brevemente)


#### Métodos HTTP
| Método HTTP | Descrição                               |
| :---------- | :-------------------------------------- |
| GET         | Lê/Consulta um recurso                  |
| POST        | Cria um recurso                         |
| PUT         | Atualiza/Altera um recurso              |
| PATCH       | Atualiza/Altera um recurso parcialmente |
| DELETE      | Remove um recurso                       |

O método de requisição **[HTTP PUT](https://developer.mozilla.org/pt-BR/docs/Web/HTTP/Methods/PUT)** cria um novo recurso ou substitui uma representação do recurso de destino com os novos dados.
A diferença entre **PUT** e **POST** é que PUT é idempotente: chamá-lo uma ou várias vezes sucessivamente terá o mesmo efeito (não é um efeito colateral), enquanto usar o POST repetidamente pode ter efeitos adicionais, como executar uma ação várias vezes.


#### Comandos cUrl relacionados com REST
| Comando cUrl    | Descrição                                                                                                                                                                                                                                                     | Exemplo                                                     |
| :-------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | :---------------------------------------------------------- |
| -i ou --include | Inclui os cabeçalhos de resposta na resposta                                                                                                                                                                                                                  | curl -i http://www.exemplo.com                              |
| -d ou --data    | Inclui dados para postar na URL. Os dados precisam ser codificados por url                                                                                                                                                                                    | curl -d "data-to-post" http://www.exemplo.com               |
| -H ou --header  | Envia o cabeçalho da solicitação para o recurso Os cabeçalhos são comuns com solicitações de API REST                                                                                                                                                         | curl -H "key:12345" http://www.exemplo.com                  |
| -X POST         | Especifica o método HTTP a ser usado com a solicitação (neste exemplo, POST). Se você usar o -d na solicitação, curl especificará automaticamente um método POST. Com solicitações GET, incluir o método HTTP é opcional, porque GET é o método padrão usado. | curl -X POST -d "resource-to-update" http://www.exemplo.com |


#### JSON Server
* JSON Server é uma aplicação que simula REST APIs com base em arquivos JSON simples
* https://github.com/typicode/json-server
* https://www.npmjs.com/package/json-server


#### Praticando
* docker build -t jsonserver .
* docker run -d --rm -it --name jsonserver-container -p 8080:8080 jsonserver
* curl -X GET http://localhost:8080/carros ou curl http://localhost:8080/carros ou http://0.0.0.0:8080/carros

* Vamos copiar o arquivo [carros.json](./aula-1/app1/carros.json) e sobrescrever dentro do container
* ls -l carros.json
* docker cp carros.json jsonserver-container:tmp/base.json
* docker ps
* docker restart jsonserver-container 
* curl -i -H "Accept: application/json" -H "Content-type: application/json" -X POST http://0.0.0.0:8080/carros -d '{"id":"9","marca":"audi","modelo":"q7"}'
* curl -i -H "Accept: application/json" -H "Content-Type: application/json" -X PUT http://0.0.0.0:8080/carros/9 -d '{"id":"9","marca":"bmw","modelo":"x1"}'
* curl -i -H "Accept: application/json" -H "Content-Type: application/json" -X PATCH http://0.0.0.0:8080/carros/9 -d '{"id":"9","modelo":"x2"}'
* curl -i -H "Accept: application/json" -H "Content-Type: application/json" -X DELETE http://0.0.0.0:8080/carros/9


## Microsserviços
### O que são microsserviços? *
São uma combinação de abordagens arquitetônicas e organizacionais apra o desenvolvimento de software em que as aplicações são compostas por serviços independentes que se comunicam por meio de APIs bem definidas.
As arquiteturas de microsserviços facilitam a escalabilidade e agilizam o desenvolvimento de aplicativos, habilitando a inovação e acelerando o tempo de introdução de novos recursos e os ciclos de implantação no mercado.

* [Microsserviços em poucas palavras](https://www.thoughtworks.com/pt-br/insights/blog/microservices-nutshell)
* [Microservices - a definition of this new architectural term](https://martinfowler.com/articles/microservices.html)


### Microsserviços, uma definição desse novo termo arquitetural
"O termo 'Arquitetura de microsserviços" surgiu nos últimos ano para descrever uma maneira específica de projetar aplicativos de software como conjuntos de serviços implementáveis independentemente. Embora não exista uma definição precisa desse estilo arquitetônico, existem certas características comuns em torno da organização, em relação à capacidade de negócios, implantação automatizada, inteligência nos terminais e controle descentralizado de linguagens e dados." Martin Fowler


### O que são microsserviços?
* [Azure](https://azure.microsoft.com/pt-br/solutions/microservice-applications) 
* [Google Cloud](https://cloud.google.com/learn/what-is-microservices-architecture?hl=pt-br)
* [IBM](https://www.ibm.com/br-pt/topics/microservices)
* [vmware](https://www.vmware.com/br/topics/glossary/content/microservices.html)
* [aws](https://aws.amazon.com/pt/microservices/)
* [Red Hat](https://www.redhat.com/pt-br/topics/microservices/what-are-microservices)


### Aplicações monolíticas vs. microsserviços
<img src="https://lh3.googleusercontent.com/o06PFnIMiTC8ek3_yVCb8kY02yZ-AinFakQ_LITcFUjpCOmqJIl1sPfVR3-xxUHQwzmnhefvdKRltcFYerK0z_NgTrwiFOqHWxYTJvHUl3s1mHIOR5WYTpQhNCKDJzzEaEROLsSZfl50bDaR7-1S8eI">

<img src="https://d1.awsstatic.com/Developer%20Marketing/containers/monolith_1-monolith-microservices.70b547e30e30b013051d58a93a6e35e77408a2a8.png">


#### Aplicação monolítica
* Para entender os benefícios dos microsserviços, considere primeiro uma aplicação monolítica.
* Os três processos (usuários, tópicos e mensagens) de uma aplicação monolítica estão altamente acoplados. Eles funcionam como um único serviços.
* Se um processo da aplicação apresentar um pico de demanda, toda a arquitetura deverá ser dimensionada. Adicionar ou melhorar recursos torna-se mais complexo à medida que a base de código cresce, o que limita a experimentação e dificulta a implementação de novas ideias.
* A disponibilidade de aplicações monolíticas também fica em risco, porque muitos processos dependentes e altamente acoplados aumentam o impacto da falha de um único processo.


#### Aplicação microsserviços
* Agora suponha que a mesma aplicação seja executada em uma arquitetura de microsserviços
* Cada processo da aplicação é criado como um componente independente que é executado como um serviço. Os serviços se comunicam usando operações de API leves.
* Cada serviço executa uma única função que pode oferecer suporte a várias aplicações. Como os serviços são executados de maneira independente, eles podem ser atualizados, implantado e dimensionados para atender à demanda por funções específicas de uma aplicação.
* Uma arquitetura de microsserviços permite iteração, automação e agilidade geral muito mais rápidas. Inicie, falhe e recupere: tudo rapidamente.


### Arquitetura monolítica
Um sistema monolítico está codificado em uma forma legada e que a complexidade está oculta dentro do monolítico, base de código. E as vezes ele cresceu em um ponto em que é muito difícil evoluir esse sistema ou criar um novo sistema. Além do fato, de termos um modelo de armazenamento que não levam as boas práticas modernas de implementação. O banco de dados tinha uma visão generalista.

Geralmente uma aplicação monolítica tinha um banco de dados que tentava resolver tudo e isso gerava problemas de escalas e de tamanho de banco de dados.


### Arquitetura microsserviços
* **Load balancer:** vai nos ajudar a balancear a carga que está sendo consumida nessa aplicação

**Obs.:** Monolito é mais fácil antes que seja mais difícil
Enquanto, microsserviços é mais difícil antes de ser mais fácil


### Aplicações monolíticas vs. microsserviços *
#### Monolítico v1 (toda funcionalidade em um aplicativo)
* **Prós:**
  * Inicialmente simples
  * Baixas latências entre processos
  * Base de código única, uma unidade de implementação
  * Eficiente quanto a recursos em pequenas escalas
* **Contras:**
  * A sobrecarga de coordenação aumenta à medida que a equipe cresce
  * Fraca imposição de modularidade
  * Escalonamento fraco
  * Implementação tudo ou nada (paralisação)
  * Longos tempos de build

#### Monolítico v2 (conjunto de camadas físicas monolíticas: front-end, servidor de aplicativos, camada de banco de dados)
* **Prós:**
  * Inicialmente simples
  * Fáceis consultas de união
  * Esquema único de implementação
  * Eficiente quanto a recursos em pequenas escalas
* **Contras:**
  * Tendência de maior acoplamento no decorrer do tempo
  * Escalonamento e redundância fracos (Tudo ou nada, somente vertical)
  * Difícil de ajustar
  * Gerenciamento de esquema tudo ou nada

#### Microsserviços (Modular, independente, relação gráficas vs. Camadas físicas, persistência isolada)
* **Prós:**
  * Cada unidade é simples
  * Escalonamento e desempenho independentes
  * Teste e implementação independentes
  * Pode ajustar o desempenho com perfeição (cache, replicação etc)
* **Contras:**
  * Muitas unidades cooperando
  * Muitas recompras pequenas
  * Exige ferramentas mais sofisticadas e gerenciamento de dependências
  * Latências de rede

* **Fonte:** [Manual de DevOps: como obter agilidade, confiabilidade e segurança em organizações tecnológicas, Capítulo 13](https://a.co/d/dCZ5Xha)


### Caso Prime Video
* [Scaling up the Prime Video audio/video monitoring service and reducing costs by 90%](https://www.primevideotech.com/video-streaming/scaling-up-the-prime-video-audio-video-monitoring-service-and-reducing-costs-by-90)
Nesse caso o Prime Video saiu de microsserviços para monolito.


### Características dos microsserviços
* **Descentralizados:** os microsserviços são descentralizados na forma como são desenvolvidos, implantados, gerenciados e operados
* **Poliglotas:** as arquiteturas de microsserviços adotam uma abordagem heterogênea para sistemas operacionais, linguagens de programação, armazenamentos de dados e ferramentas.
* **Independentes:** cada serviço do componente de uma arquitetura de microsserviços pode ser desenvolvido, implantado, operado e dimensionado sem afetar a função de outros serviços
* **Caixas pretas:** os detalhes da complexidade dos componentes de microsserviços ficam escondidos de outros componentes
* **Especializados:** cada serviço de componente é projetado para um conjunto de recursos e se concentra em resolver um problema específico
* **Você cria, você executa:** o DevOps é um princípio organizacional fundamental para microsserviços


### Checkpoint *
As aplicações de microsserviços são compostas por **serviços independentes que se comunicam por APIs bem definidas**
Os microsserviços compartilham as seguintes características:
* Descentralizados
* Independentes
* Especializados
* Poliglotas
* Caixas pretas
* Você cria, você executa


### Os principais desafios para implementar entrega contínua (Continuous Delivery)
Principais desafios segundo o State of DevOps Report 2020 apresentado pela **[Puppet](https://www.puppet.com/)** e **[CircleCI](https://circleci.com/)**:
* **Cobertura de teste incompleta:** escrever bons testes que cubram todos os cenários possíveis é quase impossível, especialmente em ambientes complexos onde há um número infinito de comportamentos de usuário, dependências, arquiteturas dinâmicas e muito mais
* **Mentalidade organizacional:** não é nenhuma surpresa que a mentalidade organizacional seja um desafio comum em cada grupo. Ouvimos muito isso em nosso trabalho com empresas, e é a única coisa com a qual os líderes seniores e profissionais estão de acordo
* **Arquitetura de aplicação fortemente acoplada:** a arquitetura de aplicação fortemente acoplada é uma das principais restrições para as equipes de entrega. Atualizar sua aplicação ou serviço requer coordenação com outras equipes, retardando a entrega de cada equipe devido às dependência complexas. O acoplamento fraco significa que os aplicativos são mais modulares =, para que as equipes possam entregar em seu próprio ritmo, usando seus próprios fluxos de trabalho.


### Arquiteturas levemente acopladas
"As organizações com esses tipos de arquiteturas orientadas a serviços, como o Google e a Amazon, têm flexibilidade e escalabilidade incríveis. Elas têm dezenas de milhares de desenvolvedores, em que pequenas equipes ainda podem ser incrivelmente produtivas." Randy Shoup, ex-diretor de engenharia do eBay, Stitch Fix, Google, WeWork
[Loosely coupled architecture](https://dora.dev/devops-capabilities/process/loosely-coupled-architecture/)


### Não existe uma solução arquitetural definitiva
Randy Shoup, também observou:
"Nâo há uma arquitetura perfeita para todos os produtos e todas as escalas. Qualquer arquitetura atende a um conjunto específico de metas ou intervalo de requisitos e restrições, como tempo de lançamento, facilidade de desenvolvimento de funcionalidades, dimensionamento etc. A funcionalidade de qualquer produto ou serviço quase certamente crescerá ao longo do tempo e nossas necessidades na arquitetura também mudarão. O que funciona na escala 1:X raramente funciona na escala 10:X ou 100:X.


## Arquitetura de Microsserviços
### Evolução da arquitetura
Monolithic (Single unit) -> SOA (Coarse-grained) -> Microservices (Fine-grained)


### Diferentes formas de implementar microsserviços
* Model/View/Controller (MVC)
* Pub-sub
* CQRS (Command Query Responsibility Segregation)


Physical (Bare metal) -> Virtualization (Virtual machines) -> Containerization (Docker) -> Serverless


**Bare metal:** uma máquina dedicada

### Arquitetura e padrões
<img src="https://microservices.io/i/MicroservicePatternLanguage.jpg">

* [A pattern language for microservices](https://microservices.io/patterns/index.html)


N-tier -> Service-oriented architecture (SOA) -> Microservices


### Teorema CAP
* O teorema CAP afirma que um sistema distribuído, composto por vários nós que armazenam dados, não pode fornecer simultaneamente mais de duas das três garantias a seguir:
  * **Consistência:** cada solicitação de leitura recebe a gravação mais recente ou um erro quando a consistência não pode ser garantida.
  * **Disponibilidade:** cada solicitação recebe um resposta sem erros, mesmo quando os nós estão inativos ou indisponíveis.
  * **Tolerância à partição:** o sistema continua operando apesar da perda de um número arbitrário de mensagens entre os nós.


### [Arquitetura Hexagonal](https://github.com/rafaelpeinado/fullcycle/tree/feature/arquitetura-hexagonal)
* Definida por Alistair Cockburn, em meados dos anos 90
* **Ideia central:** usar adaptadores para mediar a comunicação entre domínio e o restante do sistema
* **Adaptadores:** mesma ideia de padrões de projeto (GoF)
* Nome deriva do diagrama usado para ilustrar a arquitetura, formado por dois hexágonos concêntricos.

#### Objetivos
* Estabelecer uma separação clara entre:
  * Domínio limpo de tecnologia (classes do negócio)
  * Restante do sistema

**Domínio limpo de tecnologia**
* Camada de domínio não conhece:
  * Banco de dados usados pelo sistema
  * Frontend usados pelo sistema
  * Gateways de pagamentos usados pelo sistema
  * Serviços externos com os quais os sistema interage
Restante do sistema
* Interface com o usuário (Web, mobile, etc)
* Persistência e BDs
* Integrações com outros sistemas

[Engenharia de Software Moderna](https://engsoftmoderna.info/artigos/arquitetura-hexagonal.html)


#### Vantagens *
* Permite que desenvolvedores se concentrem no domínio:
  * Representa o propósito do sistema
  * Responsável pela geração de valor
* Testabilidade (mais fácil de testar domínio limpo de tecnologia)
* Maior facilidade de troca de bibliotecas, frameworks, BDs, etc.


#### Adaptadores
[Hexagonal architecture](https://alistair.cockburn.us/hexagonal-architecture/)
* Domínio "limpo" de tecnologia
  * as regras de negócios
* Adaptadores
* Restante do Sistema (tudo relacionado a tecnologia):
  * Front-end
  * Banco de dados
  * Sistemas Externos
  * Gateways de Pagamento
  * Cache
  * Bibliotecas Log
  * Pub/Sub


#### Exemplo Netflix
**A Netflix foi pioneira em implementação com sucesso em escala global nos conceitos da aula de hoje**
[Ready for changes with Hexagonal Architecture](https://netflixtechblog.com/ready-for-changes-with-hexagonal-architecture-b315ec967749)
<img src="https://miro.medium.com/v2/resize:fit:828/format:webp/1*NfFzI7Z-E3ypn8ahESbDzw.png">



### The Twelve-Factor App
[The Twelve-Factor App](https://12factor.net/)

#### Objetivos
* Minimize o esforço de configuração do novo desenvolvedor.
* Maximize a portabilidade do aplicativo.
* Implante aplicativos facilmente em plataformas de nuvem modernas.
* Manter a paridade do ambiente entre o desenvolvimento e a produção.
  * Codebase
  * Dependencies
  * Config
  * Backing services
  * Build, release, run
  * Processes
  * Port-binding
  * Concurrency
  * Disposability
  * Dev/prod parity
  * Logs
  * Administrative processes


### Domain Driven Design *
* O Domain Driven Design (DDD) é uma abordagem para o desenvolvimento de software para necessidades complexas, conectando a implementação a um modelo em evolução
* Coloca o foco principal do projeto no domínio central e na lógica do domínio
* Baseia projetos complexos em um modelo de domínio
* Inicia a colaboração criativa (usando uma linguagem ubíqua, ou UL) entre especialistas técnicos e de domínio para refinar iterativamente um modelo conceitual que trata de problemas de domínio específicos


#### DDD e Bounded Context (Contexto Limitado)
* Os Microsserviços devem ter um contexto limitado bem definido e executar apenas uma tarefa.
* Um contexto limitado encapsula um único domínio
* Um design orientado a domínio
  * Define os pontos de integração com outros domínios
  * Alinha-se bem com as características do Microsserviços
* Cuidado ao criar Microsserviços Monolíticos! 

* Vários fatores traçam limites entre os contextos, sendo a cultura humano dominante
* Contextos limitados têm conceitos não relacionados (por exemplo, tíquetes de suporte em um contexto de suporte ao cliente)
* Eles também compartilham conceitos (ex. Produtos e cliente)

[Bounded Context](https://www.martinfowler.com/bliki/BoundedContext.html)


##### Exemplo: Google Cloud Datastore
* Uma arquitetura **altamente acoplada** pode impedir a **produtividade de todos** e a capacidade de fazer mudanças com segurança.
* Por outro lado, uma **arquitetura levemente acoplada** promove produtividade e segurança com interfaces bem definidas que impõem como os módulos se conectam uns com os outros.
* Uma **arquitetura levemente acoplada** permite que equipes pequenas **e produtivas façam mudanças que possam ser implantadas de forma segura e independente.**
* Além disso, como cada serviço também tem uma API bem definida, ele facilita o teste de serviços e a criação de contratos de nível de serviço (SLAs) e de outros tipos entre equipes.


### Lei de Conway
* [Conway's Law](https://martinfowler.com/bliki/ConwaysLaw.html)
Sistemas computacionais vão espelhar a estrutura organizacional da empresa, isto é, se a empresa tem um organização monolítica, a aplicação vai ser monolítica
"Organizações que projetam sistemas (no sentido amplo usado aqui) são obrigadas
(compelidas) a produzir projetos que sejam cópias das estruturas de comunicação dessas
organizações."

**Organizational structure** reflete em **Application architecture**

### Exercício
* Uber, por exemplo

## Observações e Referências
* **[Criando Microsserviços - Sam Newman](https://a.co/d/92bwaKP)**
* **[Microsserviços Prontos Para a Produção - Susan J. Fowler](https://a.co/d/1sAwFar)**
* **[Domain-driven design - Eric Evans](https://a.co/d/eGZMvoC)**
* **[Microservices Patterns: With Examples in Java - Chris Richardson](https://a.co/d/5pT9Cxm)**
* **[Microservices in Action - Morgan Bruce/Paulo A Pereira](https://a.co/d/dh462RF)**


* **[RabbitMQ](https://rabbitmq.com/)**
* **[Qual é a função de um gateway de API?](https://www.redhat.com/pt-br/topics/api/what-does-an-api-gateway-do)**


### Exemplos de padrões de microsserviços
**AWS - Implementação de microsserviços**
* https://docs.aws.amazon.com/pt_br/whitepapers/latest/microservices-on-aws/microservices-onaws.html
* https://docs.aws.amazon.com/pt_br/whitepapers/latest/microservices-on-aws/microservices-onaws.pdf

**Microsoft Azure - Microsserviços do .NET**
* https://learn.microsoft.com/pt-br/dotnet/architecture/microservices/

**Google Cloud - Introdução a microsserviços**
* https://cloud.google.com/architecture/microservices-architecture-introduction?hl=pt-br80


### Exemplo: Cielo
[Cielo Developers](https://developercielo.github.io/)

### Exemplo: Embrapa
[AgroAPI](https://www.agroapi.cnptia.embrapa.br/portal/)

### Artigo
[Microservices: The Journey So Far and Challenges Ahead](https://ieeexplore.ieee.org/document/8354433)
